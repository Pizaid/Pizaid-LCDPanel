#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
#
# Author:   Makoto Shimazu <makoto.shimaz@gmail.com>
# URL:      https://github.com/Pizaid
# License:  2-Clause BSD License
# Created:  2014-07-17
#
import smbus
import RPi.GPIO as GPIO
import time
from threading import Timer, Lock

L_pin = 17
#U_pin = 22
R_pin = 14
D_pin = 15

bus = smbus.SMBus(1)
address = 0x04

GPIO.setmode(GPIO.BCM)
GPIO.setup(L_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
#GPIO.setup(U_pin, GPIO.IN)
GPIO.setup(R_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(D_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
class State:
    def up(self):
        return self
    def down(self):
        return self
    def right(self):
        return self
    def left(self):
        return self
    def timeout(self):
        return self

class HomeState(State):
    def __init__(self):
        print("Home State")
        bus.write_i2c_block_data(address, 254, [1])
        bus.write_i2c_block_data(address, 77, [101, 115, 115, 105, 49])
        print(time.strftime("%d/%m/%Y"))
    def up(self):
        return BatteryState()
    def down(self):
        return NetworkState()
    def timeout(self):
        print(time.strftime("%d/%m/%Y"))
class NetworkState(State):
    def __init__(self):
        print("Network State")
        bus.write_i2c_block_data(address, 254, [1])
        bus.write_i2c_block_data(address, 77, [101, 115, 115, 105, 50])
    def up(self):
        return HomeState()
    def down(self):
        return StorageState()

class StorageState(State):
    def __init__(self):
        print("Storage State")
        bus.write_i2c_block_data(address, 254, [1])
        bus.write_i2c_block_data(address, 77, [101, 115, 115, 105, 51])
    def up(self):
        return NetworkState()
    def down(self):
        return BatteryState()
    def right(self):
        return StorageDetail()

class StorageDetail(State):
    def __init__(self):
        print("Storage Detail")
        bus.write_i2c_block_data(address, 254, [1])
        bus.write_i2c_block_data(address, 77, [101, 115, 115, 105, 52])
    def left(self):
        return StorageState()
 
class BatteryState(State):
    def __init__(self):
        print("Battery State")
        bus.write_i2c_block_data(address, 254, [1])
        bus.write_i2c_block_data(address, 77, [101, 115, 115, 105, 53])
    def up(self):
        return StorageState()
    def down(self):
        return HomeState()

class StateController:
    def __init__(self, initState):
        self.timer = Timer(0.5, self.timeoutHandler)
        self.state_lock = Lock()
        self.timer.start()
        self.currentState = initState
        print(self.currentState)
        GPIO.add_event_detect(D_pin, GPIO.FALLING)
        GPIO.add_event_callback(D_pin, self.upButtonHandler, 100)
        GPIO.add_event_detect(L_pin, GPIO.FALLING)
        GPIO.add_event_callback(L_pin, self.leftButtonHandler, 100)
        GPIO.add_event_detect(R_pin, GPIO.FALLING)
        GPIO.add_event_callback(R_pin, self.rightButtonHandler, 100)
    def upButtonHandler(self, pin):
        with self.state_lock:
            if(GPIO.input(D_pin) == -1):
                self.currentState = self.currentState.up()
            elif(GPIO.input(D_pin) == 0):
                self.currentState = self.currentState.down()
        print(self.currentState)
    def leftButtonHandler(self, pin):
        with self.state_lock:
            if(GPIO.input(L_pin) == 0):
                self.currentState = self.currentState.left()
    def rightButtonHandler(self, pin): 
        with self.state_lock:
            if(GPIO.input(R_pin) == 0):
                self.currentState = self.currentState.right()
    def timeoutHandler(self):
        with self.state_lock:
            self._state = self._state.timeout()

controller = StateController(HomeState())
while True:
    pass

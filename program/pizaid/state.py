#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
#
# Author:   Makoto Shimazu <makoto.shimaz@gmail.com>
# URL:      https://github.com/Pizaid
# License:  2-Clause BSD License
# Created:  2014-08-01
#

from controller import get_controllercomm
from utils import tprint
# import RPi.GPIO as GPIO
import time
# L_pin = 17
# #U_pin = 22
# R_pin = 14
# D_pin = 15

# bus = smbus.SMBus(1)
# address = 0x04

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(L_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
# #GPIO.setup(U_pin, GPIO.IN)
# GPIO.setup(R_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
# GPIO.setup(D_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def initial_state():
    return HomeState()

  
class State:
    def updateDisplay(self):
        return self
    def up(self):
        return self
    def down(self):
        return self
    def left(self):
        return self
    def right(self):
        return self
    def center(self):
        return self

class HomeState(State):
    def __init__(self):
        tprint("HomeState")
        tprint("== Pizaid ==")
        tprint(time.strftime("%d/%m/%Y %H:%M:%S"))
        tprint("\033[3A")
    def updateDisplay(self):
        tprint("HomeState: update        ")
        tprint(time.strftime("%d/%m/%Y %H:%M:%S"))
        tprint("\033[3A")
        return self
    def up(self):
        tprint("HomeState: up        ")
        tprint(time.strftime("%d/%m/%Y %H:%M:%S"))
        tprint("\033[3A")
        return BatteryState()
    def down(self):
        tprint("HomeState: down        ")
        tprint(time.strftime("%d/%m/%Y %H:%M:%S"))
        tprint("\033[3A")
        return NetworkState()

class NetworkState(State):
    def __init__(self):
        tprint("NetworkState        ")
        self.network = get_controllercomm().network()
        tprint(self.network.get_ipv4() + "        ")
        tprint("\033[3A")
    def updateDisplay(self):
        tprint("NetworkState: update        ")
        tprint(self.network.get_ipv4() + "        ")
        tprint("\033[3A")
        return self
    def up(self):
        tprint("NetworkState: up        ")
        tprint("\033[2A")
        return HomeState()
    def down(self):
        tprint("NetworkState: down        ")
        tprint("\033[2A")
        return StorageState()

class StorageState(State):
    def __init__(self):
        tprint("Storage State        ")
        # bus.write_i2c_block_data(address, 254, [1])
        # bus.write_i2c_block_data(address, 77, [101, 115, 115, 105, 51])
        tprint(" "*30)
        tprint("\033[3A")
    def up(self):
        return NetworkState()
    def down(self):
        return BatteryState()
    def right(self):
        return StorageDetail()

class StorageDetail(State):
    def __init__(self):
        tprint("Storage Detail        ")
        tprint(" "*30)
        # bus.write_i2c_block_data(address, 254, [1])
        # bus.write_i2c_block_data(address, 77, [101, 115, 115, 105, 52])
        tprint("\033[3A")
    def left(self):
        return StorageState()

class BatteryState(State):
    def __init__(self):
        tprint("Battery State        ")
        tprint(" "*30)
        # bus.write_i2c_block_data(address, 254, [1])
        # bus.write_i2c_block_data(address, 77, [101, 115, 115, 105, 53])
        tprint("\033[3A")
    def up(self):
        return StorageState()
    def down(self):
        return HomeState()

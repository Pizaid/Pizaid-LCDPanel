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
import smbus, time
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

address_ = 0x12
bus_ = smbus.SMBus(1)
def send_str(string):
    global bus_
    hexstr = [ord(s) for s in string]
    bus_.write_i2c_block_data(address_, hexstr[0], hexstr[1:])
    return hexstr
def send_clr():
    global bus_
    bus_.write_i2c_block_data(address_, 0xFE, [0x01])    
def send_newline():
    global bus_
    bus_.write_i2c_block_data(address_, 0xFE, [0xC0])
def send_cursoroff():
    global bus_
    bus_.write_i2c_block_data(address_, 0xFE, [0xC0])    

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
        tprint(time.strftime("%H:%M:%S"))
        tprint("\033[3A")
        send_clr()
        send_str("  == Pizaid ==")
        send_newline()
        send_str(time.strftime("%H:%M:%S") + " 30% AC")
    def updateDisplay(self):
        tprint("HomeState: update        ")
        tprint(time.strftime("%H:%M:%S"))
        tprint("\033[3A")
        send_newline()
        send_str(time.strftime("%H:%M:%S"))
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
        send_clr()
        send_str("Network")
        send_newline()
        send_str(self.network.get_ipv4() + "        ")
    def updateDisplay(self):
        tprint("NetworkState: update        ")
        tprint(self.network.get_ipv4() + "        ")
        tprint("\033[3A")
        send_newline()
        send_str(self.network.get_ipv4() + "        ")
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
        tprint(" "*30)
        tprint("\033[3A")
        send_clr()
        send_str("Storage State")
        send_newline()
        send_str("XXX GB / YYY GB")
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
        tprint("\033[3A")
        send_clr()
        send_str("Storage Detail")
        send_newline()
        send_str("1:TOSHIBA,Main")
    def left(self):
        return StorageState()

class BatteryState(State):
    def __init__(self):
        tprint("Battery State        ")
        tprint(" "*30)
        tprint("\033[3A")
        send_clr()
        send_str("Battery State")
        send_newline()
        send_str("100% Ganbaru ZOI")
    def up(self):
        return StorageState()
    def down(self):
        return HomeState()

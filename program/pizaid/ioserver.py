#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
#
# Author:   Makoto Shimazu <makoto.shimaz@gmail.com>
# URL:      https://github.com/Pizaid
# License:  2-Clause BSD License
# Created:  2014-07-30
#

import threading
from utils import getch, tprint
from lcdcontroller import get_lcdcontroller
from threading import Timer
import RPi.GPIO as GPIO

def setupGPIO(pin, handler):
    pass
#     GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
#     GPIO.add_event_detect(pin, GPIO.FALLING)
#     GPIO.add_event_callback(pin, handler, 100)


class IOServer(threading.Thread):
    uPin = 23
    lPin = 19
    rPin = 15
    dPin = 21
    def __init__(self):
        threading.Thread.__init__(self)
        # tprint(self.currentState)
        GPIO.setmode(GPIO.BCM)
        setupGPIO(self.uPin, self.upButtonHandler)
        setupGPIO(self.lPin, self.leftButtonHandler)
        setupGPIO(self.rPin, self.rightButtonHandler)
        # setupGPIO(dPin, self.downButtonHandler)
        self.quit = False
        self.lcd = get_lcdcontroller()
        self.timer = Timer(0.5, self.timeoutHandler)
        
    def run(self):
        tprint("start ioserver")
        self.timer.start()
        lcd = self.lcd
        while True:
            c = getch()
            if (c == 'w'):
                lcd.up()
            elif (c == 'a'):
                lcd.left()
            elif (c == 's'):
                lcd.down()
            elif (c == 'd'):
                lcd.right()
            elif (c == ' '):
                lcd.center()
            elif (c == 'u'):
                lcd.updateDisplay()
            elif (c == 'q'):
                self.quit = True
                break
            else:
                tprint("Unknown Command")

    def upButtonHandler(self, pin = None):
        self.lcd.up()
        
    def downButtonHandler(self, pin = None):
        self.lcd.down()
        
    def leftButtonHandler(self, pin = None):
        self.lcd.left()

    def rightButtonHandler(self, pin = None):
        self.lcd.right()

    def timeoutHandler(self):
        self.lcd.updateDisplay()
        if not self.quit:
            self.timer = Timer(0.5, self.timeoutHandler)
            self.timer.start()
    

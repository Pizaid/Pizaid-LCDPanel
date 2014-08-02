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
from utils import getch
from lcdcontroller import get_lcdcontroller

class IOServer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.lcd = get_lcdcontroller()
    def run(self):
        print("start ioserver")
        lcd = self.lcd
        while True:
            c = getch()
            print("----")
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
                break
            else:
                print("Unknown Command")

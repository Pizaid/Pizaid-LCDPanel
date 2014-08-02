#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
#
# Author:   Makoto Shimazu <makoto.shimaz@gmail.com>
# URL:      https://github.com/Pizaid
# License:  2-Clause BSD License
# Created:  2014-08-01
#

from state import initial_state

class LCDController:
    def __init__(self):
        self._state = initial_state()
    def up(self):
        self._state = self._state.up()
    def down(self):
        self._state = self._state.down()
    def left(self):
        self._state = self._state.left()
    def right(self):
        self._state = self._state.right()
    def center(self):
        self._state = self._state.center()
    def updateDisplay(self):
        self._state = self._state.updateDisplay()

_controller = LCDController()
def get_lcdcontroller():
    global _controller
    return _controller

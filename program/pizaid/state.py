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

def initial_state():
    return LogoState()

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

class LogoState(State):
    def __init__(self):
        print("LogoState")
        print("== Pizaid == ")
    def updateDisplay(self):
        print("LogoState: update")
        return self
    def up(self):
        print("LogoState: up")
        return NetworkState()
    def down(self):
        print("LogoState: down")
        return NetworkState()

class NetworkState(State):
    def __init__(self):
        print("NetworkState")
        self.network = get_controllercomm().network()
        print(self.network.get_ipv4())
    def updateDisplay(self):
        print("NetworkState: update")
        print(self.network.get_ipv4())
        return self
    def up(self):
        print("NetworkState: up")
        return LogoState()
    def down(self):
        print("NetworkState: down")
        return LogoState()

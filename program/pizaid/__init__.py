#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
#
# Author:   Makoto Shimazu <makoto.shimaz@gmail.com>
# URL:      https://github.com/Pizaid
# License:  2-Clause BSD License
# Created:  2014-07-07
#

from lcdserver import LCDServer

def create_lcdserver():
    return LCDServer()

def start():
    print("Hello Pizaid!")
    print("This program is a server to display the status of RaspberryPi.")
    server = create_lcdserver()
    server.run()

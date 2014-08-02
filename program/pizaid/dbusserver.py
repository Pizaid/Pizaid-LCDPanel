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

class DBusServer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        print("start dbusserver")

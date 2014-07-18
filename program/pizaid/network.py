#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
#
# Author:   Makoto Shimazu <makoto.shimaz@gmail.com>
# URL:      https://github.com/Pizaid
# License:  2-Clause BSD License
# Created:  2014-07-18
#

import dbus

class PizaidNetwork:
    def __init__(self, dbus_object):
        self.obj = dbus_object
        self.properties = dbus.Interface(self.obj, 'com.pizaid.network.Properties')
    def get_ipv4(self):
        return self.properties.Get_ipv4()
    def get_ipv6(self):
        return self.properties.Get_ipv6()

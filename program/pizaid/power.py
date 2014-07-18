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

class PizaidPower:
    def __init__(self, dbus_object):
        self.obj = dbus_object
        self.properties = dbus.Interface(self.obj,
                                         'com.pizaid.power.Properties')
    def get_battery_percent(self):
        return self.properties.Get_battery_percent()
    def is_ac_plugin(self):
        return self.properties.Is_ac_plugin()

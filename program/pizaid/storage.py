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

class PizaidStorage:
    def __init__(self, dbus_object):
        self.obj = dbus_object
        self.properties = dbus.Interface(self.obj, 'com.pizaid.storage.Properties')
    def get_names(self):
        return self.properties.Get_names()
    def get_capacity_kb(self, name):
        return self.properties.Get_capacity_kb(name)
    def get_usage_kb(self, name):
        return self.properties.Get_usage_kb(name)
    def get_usage_percent(self, name):
        return self.properties.Get_percent_kb(name)
    def is_sync(self):
        return self.properties.Is_sync()

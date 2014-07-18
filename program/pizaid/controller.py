#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
#
# Author:   Makoto Shimazu <makoto.shimaz@gmail.com>
# URL:      https://github.com/Pizaid
# License:  2-Clause BSD License
# Created:  2014-07-12
#

import dbus
from network import PizaidNetwork


class ControllerComm:
    def __init__(self):
        self.bus = dbus.SessionBus()
    def network(self):
        obj = self.bus.get_object('com.pizaid.Controller',
                                  '/com/pizaid/controller/Network')
        return PizaidNetwork(obj)

#     def storage(self):
#         return self.bus.get_object('com.pizaid.Controller',
#                                    '/com/pizaid/controller/Storage')
#     def power(self):
#         return self.bus.get_object('com.pizaid.Controller',
#                                    '/com/pizaid/controller/Power')


#         self.network = bus.get_object(
#             'com.pizaid.Controller',
#             '/com/pizaid/controller/Network')
#         self.storage = bus.get_object(
#             'com.pizaid.Controller',
#             '/com/pizaid/controller/Storage')
#         self.power = bus.get_object(
#             'com.pizaid.Controller',
#             '/com/pizaid/controller/Power')

# bat_interface = dbus.Interface(bat_object,
# 'org.freedesktop.DBus.Properties')
# percentage = bat_interface.Get("org.freedesktop.UPower.Device",
# "Percentage"
# ).real

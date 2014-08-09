#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
#
# Author:   Makoto Shimazu <makoto.shimaz@gmail.com>
# URL:      https://github.com/Pizaid
# License:  2-Clause BSD License
# Created:  2014-07-18
#

class PizaidPower:
    def __init__(self, client):
        self.client = client
    def get_battery_percent(self):
        return self.client.power_battery_percent()
    def is_ac_plugin(self):
        return self.client.power_is_ac_plugin()

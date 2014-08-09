#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
#
# Author:   Makoto Shimazu <makoto.shimaz@gmail.com>
# URL:      https://github.com/Pizaid
# License:  2-Clause BSD License
# Created:  2014-07-18
#

class PizaidStorage:
    def __init__(self, client):
        self.client = client
    def get_names(self):
        return self.client.storage_names()
    def get_capacity_kb(self, name):
        return self.client.storage_capacity_kb(name)
    def get_usage_kb(self, name):
        return self.client.storage_usage_kb(name)
    def get_usage_percent(self, name):
        return self.client.storage_usage_percent(name)
    def is_sync(self):
        return self.client.storage_is_sync()
    def join(self, name, device):
        return self.client.storage_join(name, device)

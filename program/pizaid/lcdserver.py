#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:   Makoto Shimazu <makoto.shimaz@gmail.com>
# URL:      https://github.com/Pizaid
# License:  2-Clause BSD License
# Created:  2014-07-07
#

import time
from controller import PizaidControllerComm

class LCDServer(object):
    def run(self):
        print("running...")
        controller = PizaidControllerComm()
        network = controller.network()
        storage = controller.storage()
        power   = controller.power()
        print("IPv4: " + network.get_ipv4())
        print("Percent: " + str(power.get_battery_percent()))
        print("--Names--")
        for name in storage.get_names():
            print(name)
            print("capacity: " + str(storage.get_capacity_kb(name)))
            print("usage: " + str(storage.get_usage_kb(name)))
        time.sleep(10)


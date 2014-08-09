#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:   Makoto Shimazu <makoto.shimaz@gmail.com>
# URL:      https://github.com/Pizaid
# License:  2-Clause BSD License
# Created:  2014-07-07
#

import time
from dbusserver import DBusServer
from ioserver import IOServer
from utils import tprint

class LCDServer:
    def run(self):
        self.ioserver = IOServer()
        self.ioserver.start()
        tprint("Run io and dbus server")
        tprint("Wait to stop ioserver")
        self.ioserver.join()
#         self.dbusserver.stop()
#         tprint("running...")
#         controller = PizaidControllerComm()
#         network = controller.network()
#         storage = controller.storage()
#         power   = controller.power()
#         tprint("IPv4: " + network.get_ipv4())
#         tprint("Percent: " + str(power.get_battery_percent()))
#         tprint("--Names--")
#         for name in storage.get_names():
#             tprint(name)
#             tprint("capacity: " + str(storage.get_capacity_kb(name)))
#             tprint("usage: " + str(storage.get_usage_kb(name)))
#         time.sleep(10)


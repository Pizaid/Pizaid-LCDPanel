#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:   Makoto Shimazu <makoto.shimaz@gmail.com>
# URL:      https://github.com/Pizaid
# License:  2-Clause BSD License
# Created:  2014-07-07
#

import time
from controller import ControllerComm

class LCDServer(object):
    def __init__(self):
        pass
    def run(self):
        print("running...")
        controller = ControllerComm()
        network = controller.network()
        print("IPv4: " + network.get_ipv4())
        time.sleep(10)
        

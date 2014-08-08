#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
#
# Author:   Makoto Shimazu <makoto.shimaz@gmail.com>
# URL:      https://github.com/Pizaid
# License:  2-Clause BSD License
# Created:  2014-07-12
#

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/gen-py')

from Pizaid import ControllerService

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from network import PizaidNetwork
from storage import PizaidStorage
from power   import PizaidPower

class ControllerComm:
    def __init__(self):
        transport = TSocket.TSocket('localhost', 9090)
        self.transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        self.client = ControllerService.Client(protocol)
        self.transport.open()
    def network(self):
        return PizaidNetwork(self.client)
    def storage(self):
        return PizaidStorage(self.client)
    def power(self):
        return PizaidPower(self.client)
    def stop(self):
        self.transport.close()

_controller = ControllerComm()
def get_controllercomm():
    global _controller
    return _controller

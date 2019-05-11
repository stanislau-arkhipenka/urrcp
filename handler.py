#!/usr/bin/env python
from __future__ import division
from urrcp.settings import SERVER_ADDR
from urrcp import Urrcp

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

import Adafruit_PCA9685


class UrrcpHandler:

    null_pos = 270

    def __init__(self):
        self.pwm = Adafruit_PCA9685.PCA9685()
        self.pwm.set_pwm_freq(50)
        self.pwm.set_pwm(0, 0, self.null_pos)
        self.pwm.set_pwm(1, 0, self.null_pos)

    def ping(self):
        print('ping()')
        return True

    def set_device_speed(self, device_id, c_value):
        print(device_id, c_value)
        if device_id == "device_right":
            chn = 1
        else:
            chn = 0
        value = int(self.null_pos+round(c_value))
        self.pwm.set_pwm(chn, 0, value)


if __name__ == '__main__':
    handler = UrrcpHandler()
    processor = Urrcp.Processor(handler)
    transport = TSocket.TServerSocket(host=SERVER_ADDR, port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print('Starting the server...')
    server.serve()
    print('done.')

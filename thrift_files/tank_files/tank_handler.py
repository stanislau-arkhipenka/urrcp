#!/usr/bin/env python

from urrcp.settings import SERVER_ADDR
from urrcp.urrcp_ready.tank import Tank

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


class CalculatorHandler:
    def __init__(self):
        self.log = {}

    def ping(self):
        print('ping()')

    def c_speed(self, device_id, c_value):
        print(device_id, c_value)


if __name__ == '__main__':
    handler = CalculatorHandler()
    processor = Tank.Processor(handler)
    transport = TSocket.TServerSocket(host=SERVER_ADDR, port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)


    print('Starting the server...')
    server.serve()
    print('done.')
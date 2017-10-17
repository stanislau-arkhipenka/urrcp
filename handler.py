#!/usr/bin/env python

from urrcp.settings import SERVER_ADDR
from urrcp import Urrcp

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


class UrrcpHandler:
    def __init__(self):
        self.log = {}

    def ping(self):
        print('ping()')

    def c_speed(self, device_id, c_value):
        print(device_id, c_value)


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

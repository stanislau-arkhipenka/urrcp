import logging
import Urrcp
from classes.urrcp_handler import UrrcpHandler
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from settings import PATH_LOG, LOG_FORMAT, LOG_LEVEL, SERVER_PORT
#from robots.tank.init_schema import INIT_SCHEMA  # real tank schema
from robots.dummy_robot.init_schema import INIT_SCHEMA

logging.basicConfig(filename=PATH_LOG, level=LOG_LEVEL, format=LOG_FORMAT)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    handler = UrrcpHandler(INIT_SCHEMA)  # TODO HERE NEED TO PASS RIGHT INIT SCHEMA
    processor = Urrcp.Processor(handler)
    transport = TSocket.TServerSocket(port=SERVER_PORT)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print('Starting the server...')
    server.serve()
    print('done.')

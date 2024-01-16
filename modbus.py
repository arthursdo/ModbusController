import argparse

from pymodbus.client import ModbusTcpClient

parser = argparse.ArgumentParser()
parser.add_argument('--host', required=True, type=str, dest='host', help='IP address of the modbus server')
parser.add_argument('--port', default=502, type=int, dest='port', help='Port of the modbus server')
parser.add_argument('--address', required=True, type=int, dest='address', help='Address of the modbus server')
parser.add_argument('--slave' ,default='1',type=int, dest='slave', help='Address of the slave to write')
parser.add_argument('--value', required=True, type=int ,dest='value', help='Value to write')
args = parser.parse_args()

try:
    client = ModbusTcpClient(args.host, args.port)
    connection = client.connect()
    if connection:
        onoff = True if args.value == 1 else False
        print("Connected to modbus server at %s:%d" % (args.host, args.port))
        print("Writing %d to slave %d at address %d" % (args.value, args.slave, args.address))
        client.write_coil(args.address, onoff, args.slave )  # Modified line
    else:
        print("Failed to connect to modbus server at %s:%d" % (args.host, args.port))
        print("Exiting...")
except Exception as e:
    print(e)

client.close()
import sys
import socket
import struct

packer = struct.Struct('20s l')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
seeder_address = ('localhost', 8082)
sock.bind(seeder_address)


tracer_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tracer_address = ('localhost', 8081)
tracer_sock.connect(tracer_address)

packed_addr = packer.pack(bytes(seeder_address[0], "UTF8"), seeder_address[1])
tracer_sock.sendall(packed_addr)

tracer_sock.close()


packer = struct.Struct('20s')


sock.listen();

connection, leecher_address = sock.accept()
print(str(leecher_address))
connection.sendall(packer.pack('ZH'))
print("elküldtam a ZH szöveget")


sock.close()

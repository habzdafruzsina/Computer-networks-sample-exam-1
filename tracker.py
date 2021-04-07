import sys
import socket
import select
import struct

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8081)
sock.bind(server_address)

packer = struct.Struct('20s l')


sock.listen()
connection1, seeder_address = sock.accept()

data = connection1.recv(packer.size)
seeder_addr = packer.unpack(data)



sock.listen()
connection2, leecher_address = sock.accept()


packed_addr = packer.pack(seeder_addr[1].encode('utf-8'), seeder_addr[0])
connection2.sendall(packed_addr)
print("Elküldtem a seeder címét")


sock.close()



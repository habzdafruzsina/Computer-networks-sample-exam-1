import sys
import socket
import struct

tracer_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tracer_address = ('localhost', 8081)
tracer_sock.connect(tracer_address)

unpacker1 = struct.Struct('20s l')
unpacker2 = struct.Struct('20s')

data = tracer_sock.recv(unpacker1.size)

unpacked_data = unpacker1.unpack(data)
s_a = [unpacked_data[0].decode('utf-8').rstrip('\x00'), unpacked_data[1]]
seeder_address = (s_a[0], s_a[1])
print("Megkaptam a seeder címét: " + str(seeder_address))

seeder_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
seeder_sock.connect(seeder_address)
print("Csatlakoztam a seederhez")

data = seeder_sock.recv(unpacker2.size)
print("Megkaptam az üzenetet")
print(unpacker2.unpack(data).encode('utf-8'))
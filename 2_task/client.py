from socket import *
import struct
import time

host = 'localhost'
port = 123

sock = socket(AF_INET, SOCK_DGRAM)
sock.sendto(b'',(host, port))
data = sock.recvfrom(1024)
t = struct.unpack(">q",data[0])[0]
print(time.localtime(t))
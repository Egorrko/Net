from socket import *
import time
import struct

host = 'localhost'
port = 123
file = open("shift.txt")
shift = int(file.read())
file.close()
print("Сдвиг = ", shift, " секунд")

conn = socket(AF_INET, SOCK_DGRAM)
conn.bind((host, port))


while True:
  request = conn.recvfrom(1024)
  print(request)
  conn.sendto(struct.pack(">q",int(time.time()+shift)), request[1])
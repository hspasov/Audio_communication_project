import socket
import numpy

UDP_IP = "192.168.1.1"
UDP_PORT = 5005
MESSAGE = numpy.random.rand(3, 2)

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)
print("message:", MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

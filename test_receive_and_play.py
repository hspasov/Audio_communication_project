import socket
import numpy
import sounddevice as sd

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                                         socket.SOCK_DGRAM) # UDP
sock.bind(("", UDP_PORT))

while True:
    data, addr = sock.recvfrom(640000) # buffer size in bytes
    numpyarray = numpy.fromstring(data, dtype='float32')
    sd.play(numpyarray, 48000)
    sd.wait()


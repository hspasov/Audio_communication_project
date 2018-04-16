import sounddevice as sd
import socket
import numpy
import time

UDP_IP = "192.168.1.2"
UDP_PORT = 5005

delay = 1
switch = False

sock = socket.socket(socket.AF_INET, # Internet
                                 socket.SOCK_DGRAM) # UDP

recording1 = sd.rec(delay * 48000, samplerate=48000, channels=1, dtype='float32')

while True:
    sd.wait()
    print('Recording finished')
    print("UDP target IP:", UDP_IP)
    print("UDP target port:", UDP_PORT)
    print("message length:", recording1.size)
    split_recording = numpy.array_split(recording1, 15)
    for chunk in split_recording:
        print ('hey')
        print('chunk size:', chunk.size)
        print("it starts with: ", chunk[0])
        print('another size: ', len(bytearray(chunk)))
        sock.sendto(chunk, (UDP_IP, UDP_PORT))
    recording1 = sd.rec(delay * 48000, samplerate=48000, channels=1, dtype='float32')



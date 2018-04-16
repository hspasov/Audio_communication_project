import sounddevice as sd
import socket
import numpy
import time

UDP_IP = "192.168.1.2"
UDP_PORT = 5005

myrecording = sd.rec(5 * 48000, samplerate=48000, channels=1, dtype='float32')

sd.wait()
print('Recording finished')

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)
print("message length:", myrecording.size)


sock = socket.socket(socket.AF_INET, # Internet
                                 socket.SOCK_DGRAM) # UDP

split_recording = numpy.array_split(myrecording, 15)
for chunk in split_recording:
    print ('hey')
    print('chunk size:', chunk.size)
    print("it starts with: ", chunk[0])
    print('another size: ', len(bytearray(chunk)))
    sock.sendto(chunk, (UDP_IP, UDP_PORT))
    


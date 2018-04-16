import sounddevice as sd
import socket
import numpy
import time
import threading

UDP_IP = "192.168.1.2"
UDP_PORT = 5005

class DataSender(threading.Thread):
    def run(self):        
        delay = 1
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
                print('size: ', len(bytearray(chunk)))
                sock.sendto(chunk, (UDP_IP, UDP_PORT))
            recording1 = sd.rec(delay * 48000, samplerate=48000, channels=1, dtype='float32')

class DataReceiver(threading.Thread):
    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(("", UDP_PORT))
        while True:
            data = sock.recvfrom(640000) # buffer size in bytes
            print("received message size:", len(data))
            numpyarray = numpy.fromstring(data, dtype="float32")
            print("length", numpyarray.size)
            sd.play(numpyarray, 48000)
            sd.wait()

DataSender().start()
DataReceiver().start()

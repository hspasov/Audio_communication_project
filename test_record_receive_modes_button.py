import sounddevice as sd
import socket
import numpy
import time
import threading
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

UDP_IP = "192.168.1.2"
UDP_PORT = 5005

send_mode = False;
data_receiver_finished = False

class DataReceiver(threading.Thread):
    def run(self):
        print("Starting data receiver")
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(("", UDP_PORT))
        while not send_mode:
            data = sock.recvfrom(640000) # buffer size in bytes
            print("received message size:", len(data))
            numpyarray = numpy.fromstring(data, dtype="float32")
            print("length", numpyarray.size)
            sd.play(numpyarray, 48000)
            sd.wait()
        print("Going out of data receiver")
        data_receiver_finished = True


def send_data(something):
    print("Start send mode")
    send_mode = True
    GPIO.remove_event_detect(24)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    delay = 1
    GPIO.output(23, GPIO.HIGH)
    recording1 = sd.rec(delay * 48000, samplerate=48000, channels=1, dtype='float32')
    sd.wait()
    split_recording = numpy.array_split(recording1, 15)
    for chunk in split_recording:
        print('size: ', len(bytearray(chunk)))
        sock.sendto(chunk, (UDP_IP, UDP_PORT))
    send_mode = False
    GPIO.output(23, GPIO.LOW)
    if data_receiver_finished:
        DataReceiver.start()
    GPIO.add_event_detect(24, GPIO.RISING, callback=send_data)
    print("End send mode")

GPIO.add_event_detect(24, GPIO.RISING, callback=send_data)

DataReceiver().start()

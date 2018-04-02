import sounddevice as sd

myrecording = sd.rec(5 * 48000, 48000, 1)

sd.wait()
print('Recording finished')

sd.play(myrecording, 48000)

while True:
    a = 1

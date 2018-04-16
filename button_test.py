import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(23, GPIO.OUT)

try:
    while True:
        reading = GPIO.input(24)
        GPIO.output(23, reading)
        if reading:
            print("ON")
        else:
            print("OFF")
except KeyboardInterrupt:
    GPIO.cleanup()

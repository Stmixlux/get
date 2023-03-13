import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.OUT)
GPIO.setup(22, GPIO.IN)

# while True:
#     GPIO.output(2, 1)
#     time.sleep(1)
#     GPIO.output(2, 0)
#     time.sleep(1)

while True:
    GPIO.output(2, GPIO.input(22))
    time.sleep(0.1)




import RPi.GPIO as GPIO
import time


def d2b(num, rank=8):
    return [int(bite) for bite in bin(num % 2 ** rank)[2:].zfill(rank)]


GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

[GPIO.setup(pin, GPIO.OUT) for pin in dac]

try:
    t = int(input()) / 512
    while True:
        for i in range(0, 256):
            signal = d2b(i)
            [GPIO.output(dac[i], signal[i]) for i in range(8)]
            time.sleep(t)
        for i in range(256, 0, -1):
            signal = d2b(i)
            [GPIO.output(dac[i], signal[i]) for i in range(8)]
            time.sleep(t)
finally:
    [GPIO.output(pin, 0) for pin in dac]
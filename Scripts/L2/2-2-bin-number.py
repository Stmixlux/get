import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

[GPIO.setup(led, GPIO.OUT) for led in dac]

while True:
    cm = input()
    if cm == "b":
        break
    elif cm == "c":
        [GPIO.output(led, 0) for led in dac]
    else:
        number = ([0] * 8 + list(map(int, bin(int(cm))[2:])))[-8:]
        [GPIO.output(dac[i], number[i]) for i in range(8)]

[GPIO.output(led, 0) for led in dac]

GPIO.cleanup()
    
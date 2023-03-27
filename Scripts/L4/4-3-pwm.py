import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

[GPIO.setup(pin, GPIO.OUT) for pin in dac]
pwm_port = 21
GPIO.setup(pwm_port, GPIO.OUT)

p = GPIO.PWM(pwm_port, 50)

try:
    p.start(0)
    while True:
        dc = float(input())
        p.ChangeDutyCycle(dc)
finally:
    p.stop()
    [GPIO.output(pin, 0) for pin in dac]
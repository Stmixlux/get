import RPi.GPIO as GPIO


def d2b(num, rank=8):
    return [int(bite) for bite in bin(num % 2 ** rank)[2:].zfill(rank)]


GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

[GPIO.setup(pin, GPIO.OUT) for pin in dac]

try:
    while True:
        command = input()
        if command == "q":
            break
        
        if "." in command or "," in command:
            print("Нужно вводить целое число")
            continue

        if not command.isnumeric():
            print("Нужно вводить числовое значение")
            continue
        
        if command[0] == "-":
            print("Должно быть положительное значение")
            continue

        if int(command) >= 256:
            print("Желательно вводить значения в диапазоне от 0 до 255")
        
        signal = d2b(int(command))
        [GPIO.output(dac[i], signal[i]) for i in range(8)]
        print("Ожидемое напряжение {:.2f}В".format(3.3 * (int(command) % 256) / 256))
        
finally:
    [GPIO.output(pin, 0) for pin in dac]
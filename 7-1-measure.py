import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13
max_volt = 3.3

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

def decimal2bin(value):
    return[int(element) for element in bin(value)[2:].zfill(8)]

def adc1():
    value = 128
    GPIO.output(dac, decimal2bin(value))
    time.sleep(0.01)
    if GPIO.input(14) == 1:
        value -= 128

    value += 64
    GPIO.output(dac, decimal2bin(value))
    time.sleep(0.01)
    if GPIO.input(14) == 1:
        value -= 64

    value += 32
    GPIO.output(dac, decimal2bin(value))
    time.sleep(0.01)
    if GPIO.input(14) == 1:
        value -= 32

    value += 16
    GPIO.output(dac, decimal2bin(value))
    time.sleep(0.01)
    if GPIO.input(14) == 1:
        value -= 16

    value += 8
    GPIO.output(dac, decimal2bin(value))
    time.sleep(0.01)
    if GPIO.input(14) == 1:
        value -= 8

    value += 4
    GPIO.output(dac, decimal2bin(value))
    time.sleep(0.01)
    if GPIO.input(14) == 1:
        value -= 4

    value += 2
    GPIO.output(dac, decimal2bin(value))
    time.sleep(0.01)
    if GPIO.input(14) == 1:
        value -= 2

    value += 1
    GPIO.output(dac, decimal2bin(value))
    time.sleep(0.01)
    if GPIO.input(14) == 1:
        value -= 1

    return value

def lightUp(voltage):
    num_leds = int(voltage/3.28 * 8)
    for i in range(8):
        if i < num_leds:
            GPIO.output(leds[i], 1)
        else:
            GPIO.output(leds[i], 0)

try:
    values = []
    time_start = time.time()
    GPIO.output(troyka, GPIO.HIGH)

    print("Зарядка")
    while adc1() < 200:
        values.append(adc1())

    print("Разрядка")
    GPIO.output(troyka, GPIO.LOW)

    while adc1() > 100:
        values.append(adc1())

    time_stop = time.time()
    duration = time_stop - time_start

    plt.plot(values)

    plt.title("Зарядка/разрядка конденсатора")

    plt.grid(True)
    plt.show()

    values_str = [str(i) for i in values]
    with open("data.txt", "w") as f:
        f.write("\n".join(values_str))

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    T = duration / len(values)
    qs = max_volt / 256
    with open("settings.txt", "w") as out:
        out.write(f"qs = {qs}, T = {T}")
    print(f"T = {T}, qs = {qs}")

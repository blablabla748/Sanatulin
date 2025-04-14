import RPi.GPIO as GPIO
import time
import math
dac =[8,11,7,1,0,5,12,6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
def dec2bin(value):
    return [int(bit) for bit in bin(value)[2::].zfill(8)]
def calc():
    while True:
        try:
            period=float(input())
            if period<=0:
                print("надо положительное")
                continue 
            return period
        except ValueError:
            print()
try:
    period=calc()
    samples=256
    delay=period/(2*samples)
    print(f" генерация треугольного {period} ")
    print("ctrl+c чтобы остановить")
    while True:
        for value in range(0,256,1):
            GPIO.output(dac,dec2bin(value))
            time.sleep(delay)
        for value in range(255,1,-1):
            GPIO.output(dac,dec2bin(value))
            time.sleep(delay)
except KeyboardInterrupt:
    print("stopped by me")
finally:
    GPIO.output(dac,0)
    GPIO.cleanup()
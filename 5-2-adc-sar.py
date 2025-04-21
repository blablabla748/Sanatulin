import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac=[8,11,7,1,0,5,12,6]
comp=14
troyka=13
max_volt=3.3
GPIO.setup(dac,GPIO.OUT)
GPIO.setup(troyka,GPIO.OUT,initial=1)
GPIO.setup(comp,GPIO.IN)
def decimal2bin(value):
    return[int(element)for element in bin(value)[2:].zfill(8)]
def adc():
    tim=0.1
    value=128
    GPIO.output(dac,decimal2bin(value))
    time.sleep(tim)
    if GPIO.input(comp) ==1:
        value-=128
    value+=64
    GPIO.output(dac,decimal2bin(value))
    time.sleep(tim)
    if GPIO.input(comp) ==1:
        value-=64
    value+=32
    GPIO.output(dac,decimal2bin(value))
    time.sleep(tim)
    if GPIO.input(comp) ==1:
        value-=32
    value+=16
    GPIO.output(dac,decimal2bin(value))
    time.sleep(tim)
    if GPIO.input(comp) ==1:
        value-=16
    value+=8
    GPIO.output(dac,decimal2bin(value))
    time.sleep(tim)
    if GPIO.input(comp) ==1:
        value-=8
    value+=4
    GPIO.output(dac,decimal2bin(value))
    time.sleep(tim)
    if GPIO.input(comp) ==1:
        value-=4
    value+=2
    GPIO.output(dac,decimal2bin(value))
    time.sleep(tim)
    if GPIO.input(comp) ==1:
        value-=2
    value+=1
    GPIO.output(dac,decimal2bin(value))
    time.sleep(tim)
    if GPIO.input(comp) ==1:
        value-=1
    return value
try:
    while True:
        digital_value=adc()
        voltage=digital_value*max_volt/256
        print("значение нпряжния {} В для числа {}".format(voltage,digital_value))
        time.sleep(0.01)
finally:
    GPIO.output(dac,0)
    GPIO.cleanup()    
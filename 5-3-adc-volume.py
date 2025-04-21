import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac=[8,11,7,1,0,5,12,6]
comp=14
troyka=13
max_volt=3.3
leds=[2,3,4,17,27,22,10,9]
GPIO.setup(dac,GPIO.OUT)
GPIO.setup(leds,GPIO.OUT)
GPIO.setup(troyka,GPIO.OUT,initial=1)
GPIO.setup(comp,GPIO.IN)
def decimal2bin(value):
    return[int(element) for element in bin(value)[2:].zfill(8)]
def lightup(voltage):
    num_leds=int(voltage/3.28*8)
    for i in range(8):
        if i<num_leds:
            GPIO.output(leds[i],1)
        else:
            GPIO.output(leds[i],0)
def adc1():
    value=0
    for i in range (7,-1,-1):
        value+=2**i
        GPIO.output(dac,decimal2bin(value))
        time.sleep(0.01)
        if GPIO.input(comp)==1:
            value -=2**i
    return value
def adc2():
    for value in range(256):
        GPIO.output(dac,decimal2bin(value))
        time.sleep(0.001)
        if GPIO.input(comp)==1:
            return value
    return 255
try:
    while   True:
        digital_value=adc1()
        voltage=digital_value*max_volt/256
        print("Значние напрядния {}В для числа {}".format(voltage,digital_value))
        lightup(voltage)
        time.sleep(0.01)
finally:
    GPIO.output(dac,0)
    GPIO.cleanup()
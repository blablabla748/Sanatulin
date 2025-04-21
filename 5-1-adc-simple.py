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
    return[int(element) for element in bin(value)[2:].zfill(8)]
def adc():
    for value in range(256):
        GPIO.output(dac,decimal2bin(value))
        time.sleep(0.001)
        if GPIO.input(comp)==1:
            return value
    return 255
try:
    while True:
        digital_value=adc()
        voltage=digital_value*max_volt/256
        print("Значение напряжния {} В для числа {}".format(voltage,digital_value))
finally:
    GPIO.output(dac,0)
    GPIO.cleanup()
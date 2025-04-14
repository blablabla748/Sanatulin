
import RPi.GPIO as GPIO
import sys
dac=[8,11,7,1,0,5,12,6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2::].zfill(8)]
def calc(value):
    return 3.244*value/255
try:
    while True:
        user_input= input()
        if user_input.lower()== 'q':
            break
        try:
            number=int(user_input)
        except ValueError:
            print('щшибка')
            continue
        if number < 0:
            print('щтрицательное число')
        elif number > 255:
            print('слишком большое')
            continue
        binary_value=decimal2binary(number)
        GPIO.output(dac,binary_value)
        voltage=calc(number)
        print(f"напряжение: {voltage:.2f}")
finally:
    GPIO.output(dac,0)
    GPIO.cleanup()
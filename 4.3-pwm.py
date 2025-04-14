import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
pin =24
GPIO.setup(pin,GPIO.OUT)
pwm=GPIO.PWM(pin,1000)
pwm.start(0)
try:
    while True:
        u_input=input()
        if u_input=='q':
            break
        try:
            cycle=float(u_input)
            if cycle<0 or cycle >100:
                print("ощибка")
            pwm.ChangeDutyCycle(cycle)
            voltage=3.3*cycle/100
            print('напряжение',voltage)
        except ValueError:
            print('ошибка')
finally:
    pwm.stop()
    GPIO.cleanup()
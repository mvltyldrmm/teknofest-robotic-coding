import RPi.GPIO as GPIO

mode=GPIO.getmode()

GPIO.cleanup()

motor1=24 #ileri motorları
motor2 = 23 #ileri motorları
motor3=22 #sag
motor4 = 21 #sol
motor5 = 20 #asagi
motor6 = 19 #yukari

GPIO.setmode(GPIO.BOARD)
GPIO.setup(motor1, GPIO.OUT)
GPIO.setup(motor2, GPIO.OUT)
GPIO.setup(motor3, GPIO.OUT)
GPIO.setup(motor4, GPIO.OUT)
GPIO.setup(motor5, GPIO.OUT)
GPIO.setup(motor6, GPIO.OUT)

def ilerle():
    GPIO.output(motor1, GPIO.HIGH)
    GPIO.output(motor2, GPIO.HIGH)
    GPIO.output(Forward, GPIO.LOW)
    GPIO.output(Forward, GPIO.LOW)

def sag():
    GPIO.output(motor3, GPIO.HIGH)
    GPIO.output(motor3, GPIO.LOW)

def sol():
    GPIO.output(motor4, GPIO.HIGH)
    GPIO.output(motor4, GPIO.LOW)

def asagi():
    GPIO.output(motor5, GPIO.HIGH)
    GPIO.output(motor5, GPIO.LOW)

def yukari():
    GPIO.output(motor6, GPIO.HIGH)
    GPIO.output(motor6, GPIO.LOW)

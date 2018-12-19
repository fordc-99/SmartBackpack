import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

red = 32
green = 36

GPIO.setup(red,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)

while True:
    print "LED on"
    GPIO.output(red,GPIO.HIGH)
    GPIO.output(green,GPIO.HIGH)

    time.sleep(1)

    print "LED off"
    GPIO.output(red,GPIO.LOW)
    GPIO.output(green,GPIO.LOW)

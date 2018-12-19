import RPi.GPIO as GPIO
import time

#set constants
BUTTON_INPUT = 11 
#end constants

#setup code
GPIO.setmode(GPIO.BCM)

GPIO.setup(BUTTON_INPUT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#end setup

#button
while True:
    input_state = GPIO.input(BUTTON_INPUT)
    if input_state == False:
        print('Button Pressed')
        time.sleep(0.2)
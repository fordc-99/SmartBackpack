import RPi.GPIO as GPIO
import time

#set constants
BUTTON_INPUT = 11
FSR_INPUT = 16

BUTTON_LED = 32
FSR_LED = 36
#end constants

#setup code
GPIO.setmode(GPIO.BCM)

GPIO.setup(BUTTON_INPUT, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(BUTTON_LED, GPIO.OUT)
GPIO.setup(FSR_LED, GPIO.OUT)
#end setup

#button
while True:
    input_state = GPIO.input(BUTTON_INPUT)
    turn_off(BUTTON_LED)
    if input_state == False:
        turn_on(BUTTON_LED)
        print('Button Pressed')
        time.sleep(0.2)
        turn_off(BUTTON_LED)
                

def turn_on(port_num):
    GPIO.output(port_num, GPIO.HIGH)
    
def turn_off(port_num):
    GPIO.output(port_num, GPIO.LOW))

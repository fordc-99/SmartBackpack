import RPi.GPIO as GPIO
import time

from pushbullet import Pushbullet

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

pb= Pushbullet('o.jq7HoVKz2DCWJ1Vxem7E9ZvRRVEKz27T')
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
        pb.push_note("SOS", "You requested help")
    
    fsr_state = GPIO.input(FSR_INPUT)
    turn_off(FSR_LED)
    if (fsr_state == False):
        turn_on(FSR_LED)
        print("fsr activated")
        time.sleep(0.2)
        turn_off(FSR_LED)
        push = pb.push_note("Dehydration", "You need water")
                

def turn_on(port_num):
    GPIO.output(port_num, GPIO.HIGH)
    
def turn_off(port_num):
    GPIO.output(port_num, GPIO.LOW))

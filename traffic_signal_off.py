# python traffic_signal.py

# This script is supposed to turn the traffic lights off, but it doesn't work...

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)

# Turn off the lights
GPIO.output(2,GPIO.LOW)
GPIO.output(3,GPIO.LOW)
GPIO.output(4,GPIO.LOW)

# Cleanup GPIO pins on program exit
GPIO.cleanup()




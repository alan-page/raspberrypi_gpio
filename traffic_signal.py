# sudo python traffic_signal.py

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)

# Fraction or multiple of seconds for each ON state in the loop (1 = 10 seconds of red light)
timefactor = 0.5

while True:
    print "Red"
    GPIO.output(2,GPIO.HIGH)
    GPIO.output(3,GPIO.LOW)
    durationR = timefactor * 10
    time.sleep(durationR)

    print "Green"
    GPIO.output(2,GPIO.LOW)
    GPIO.output(4,GPIO.HIGH)
    durationG = timefactor * 10
    time.sleep(durationG)

    print "Yellow"
    GPIO.output(4,GPIO.LOW)
    GPIO.output(3,GPIO.HIGH)
    durationY = timefactor * 4    
    time.sleep(durationY)

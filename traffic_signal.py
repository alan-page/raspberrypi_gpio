# python traffic_signal.py

# Traffic signal simulator

import RPi.GPIO as GPIO
print "Imported RPi.GPIO"

# For sleep
import time
print "Imported time"

# For getting hours and minutes
from datetime import datetime
print "Imported datetime"

GPIO.setmode(GPIO.BCM)

# Don't suppress any warnings. Yes, it's a double negative...
#GPIO.setwarnings(False)

# Red on pin 2
red = 2
GPIO.setup(red, GPIO.OUT)

# Yellow on pin 3
yellow = 3
GPIO.setup(yellow, GPIO.OUT)

# Green on pin 4
green = 4
GPIO.setup(green, GPIO.OUT)

# Fraction or multiple of seconds for each ON state in the loop (1 = 10 seconds of red light)
timefactor = 1

try:
    while True:
        # Flash the yellow lights late at night
#        print "About to get the datetime"
        d = datetime.now()
#        print d
        if d.hour < 6 or d.hour > 21:
            GPIO.output(green,GPIO.LOW)
            GPIO.output(red,GPIO.LOW)
            GPIO.output(yellow,GPIO.LOW)

            time.sleep(.7)
            GPIO.output(yellow,GPIO.HIGH)
            time.sleep(.7)
            GPIO.output(yellow,GPIO.LOW)
            time.sleep(.7)

        else:
            print "Red"
            GPIO.output(yellow,GPIO.LOW)
            GPIO.output(red,GPIO.HIGH)
            durationR = timefactor * 10
            time.sleep(durationR)

            print "Green"
            GPIO.output(red,GPIO.LOW)
            GPIO.output(green,GPIO.HIGH)
            durationG = timefactor * 10
            time.sleep(durationG)

            print "Yellow"
            GPIO.output(green,GPIO.LOW)
            GPIO.output(yellow,GPIO.HIGH)
            durationY = timefactor * 4
            time.sleep(durationY)

except KeyboardInterrupt:
    # Special Ctrl-C code
    # This code works and displays the message properly
    print "...Ctrl-C..."
    GPIO.output(red,GPIO.LOW)
    GPIO.output(yellow,GPIO.LOW)
    GPIO.output(green,GPIO.LOW)

except:
    # Other interrupts (errors maybe?)
    # How to trigger this?
    print "Non Ctrl-C interruption! "

finally:
    # Turn off the lights
    #   ...this  doesn't appear work...
    GPIO.output(red,GPIO.LOW)
    GPIO.output(yellow,GPIO.LOW)
    GPIO.output(green,GPIO.LOW)

    # Cleanup GPIO pins on program exit
    GPIO.cleanup()




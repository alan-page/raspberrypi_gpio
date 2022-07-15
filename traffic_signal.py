# python traffic_signal.py

# Traffic signal simulator

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

# Don't suppress any warnings. Yes, it's a double negative...
#GPIO.setwarnings(False)

# Red
GPIO.setup(2,GPIO.OUT)
red = 2

# Yellow
GPIO.setup(3,GPIO.OUT)
yellow = 3

# Green
GPIO.setup(4,GPIO.OUT)
green = 4

# Fraction or multiple of seconds for each ON state in the loop (1 = 10 seconds of red light)
timefactor = 1

try:
    while True:
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




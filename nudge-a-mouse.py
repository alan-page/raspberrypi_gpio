# Using Parallax Basic Stamp servo
# 50 Hz (20 ms) pulse train
# Min duty cycle: 2.5 (0.5 ms pulse)
# Max duty cycle: 10 (2.0 ms pulse)
# 9v DC power (grounded to rPi GND)

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)   # Set up PWM pin for the servo
p = GPIO.PWM(13, 50)       # Set up the pulse train at 50Hz (20 ms)

GPIO.setup(26, GPIO.IN)    # Set up the activate button

# Start the servo with 4% duty cyle: 4% * 20ms = 0.8 ms DC
p.start(4)
print("DC: 4")


try:
    while True:
        while GPIO.input(26) == 0:

# 8% duty cyle: 8% * 20ms = 1.6 ms DC
            print ("'Nudge-Mouse' is ON")
            time.sleep(2)

            p.ChangeDutyCycle(8)
            print("DC: 8 - Nudge the mouse")
            time.sleep(0.4)

            p.ChangeDutyCycle(4)
            print("DC: 4 - Return")
            time.sleep(0.5) #Return to start

            p.ChangeDutyCycle(0) # Zero duty cycle  while waiting with switch on
            print ("Wait a minute-ish before nudging the mouse again...")
            time.sleep(5)
            
# Zero duty cycle to stop pwm while waiting (no jitter)
        p.ChangeDutyCycle(0)
        print("DC: zero - 'Nudge-a-Mouse' is off")
        time.sleep(1)

except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()

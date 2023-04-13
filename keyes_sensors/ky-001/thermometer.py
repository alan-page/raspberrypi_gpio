# Python 3 only!!

# Notes
# From https://sensorkit.joy-it.net/en/sensors/ky-001
# For this to work, set up the one wire configuration. 
# The file "/boot/config.txt" must be edited
# Add the following to the end of the file:
#   dtoverlay=w1-gpio,gpiopin=17
# Then reboot the pi

# Strangely, when using parasitic power, the temp is always 185 F...

# coding=utf-8
# Required modules are imported and set up
import glob
import time
import datetime
from time import sleep
import RPi.GPIO as GPIO
 
# At this point the pause (in seconds) between the individual measurements can be set
sleeptime = 60
 
# The One-Wire input pin is declared and the integrated PullUp resistor is activated
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
 
# After activation of the Pull-UP resistor it waits
# until the communication with the DS18B20 sensor is established.
print ("Waiting for initialization...")
 
base_dir = '/sys/bus/w1/devices/'
while True:
    try:
        device_folder = glob.glob(base_dir + '28*')[0]
        break
    except IndexError:
        sleep(0.5)
        continue
device_file = device_folder + '/w1_slave'
 
 
# Function is defined, with which the current measured value can be read out at the sensor.
def TemperaturMessung():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
# For initialization, the sensor is read out "blind" once.
TemperaturMessung()
 
# The temperature evaluation: On the Raspberry Pi, detected one-Wire slaves are assigned to a separate subfolder in the folder
# /sys/bus/w1/devices/ are assigned to an own subfolder. In this folder is the file w1-slave
# in which the data sent over the one-wire bus is stored.
# In this function these data are analyzed and the temperature is read out and output.
def TemperaturAuswertung():
    lines = TemperaturMessung()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = TemperaturMessung()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0

        # Fahrenheit: Double it and add 30?
        temp_f = ((temp_c * 9) / 5) + 32
        temp_f_format = "{:.1f}".format(temp_f)
        return temp_f_format

# Main program loop
# The measured temperature is output to the console - between the individual measurements
# is a pause, the length of which can be set with the "sleeptime" variable
try:
    while True:
        temp_value = TemperaturAuswertung()
        # Cast string of "xx.y" value to a float, then an integer (and add 1 to align the bar end)
        temp_value_int = int(float(temp_value)) + 1
        temp_bar_string = ""
        for t in range(0, temp_value_int):
            temp_bar_string += "="

        print (datetime.datetime.now())
        print ("Indoor Temperature:", temp_value, "°F")
        print ("0    +    10   +    20   +    30   +    40   +    50   +    60   +    70   +    80   +    90   +    100 F")
        print (temp_bar_string)

        time.sleep(sleeptime)

except KeyboardInterrupt:
    GPIO.cleanup

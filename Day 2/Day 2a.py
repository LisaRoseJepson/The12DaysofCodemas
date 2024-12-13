'''
Turning LEDS on/off/flashing
'''

# Imports
import time
from machine import Pin

# Set up Pin
red = Pin(20, Pin.OUT)
yellow = Pin(19, Pin.OUT)
green = Pin(18, Pin.OUT)

count = 0

# Flash on/off 10 times
while count < 10:
    red.value(1)
    yellow.value(1)
    green.value(1)
    time.sleep(1)
    red.value(0)
    yellow.value(0)
    green.value(0)
    time.sleep(1)
    
    count += 1

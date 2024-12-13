'''
Cycling through LEDs
'''

# Imports
import time
from machine import Pin

# Set up Pin
red = Pin(20, Pin.OUT)
yellow = Pin(19, Pin.OUT)
green = Pin(18, Pin.OUT)

# Turn all LEDs off
red.value(0)
yellow.value(0)
green.value(0)

# Cycle through lights
while True:
    red.value(1)
    time.sleep(0.5)
    red.value(0)
    yellow.value(1)
    time.sleep(0.5)
    yellow.value(0)
    green.value(1)
    time.sleep(0.5)
    green.value(0)



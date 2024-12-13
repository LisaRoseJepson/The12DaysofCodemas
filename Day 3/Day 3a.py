'''
Buttons to toggle LEDs on/off
'''

# Imports
from machine import Pin
import time

# Set up PINs LEDS
red = Pin(20, Pin.OUT)
yellow = Pin(19, Pin.OUT)
green = Pin(18, Pin.OUT)

# Set up PINs buttons
button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(3, Pin.IN, Pin.PULL_DOWN)

# Set LEDs to off
red.value(0)
yellow.value(0)
green.value(0)

# Light one LED per button
while True:
    if button1.value() == 1:
        red.toggle()
    elif button2.value() == 1:
        yellow.toggle()
    elif button3.value() == 1:
        green.toggle()
        
    time.sleep(0.2)
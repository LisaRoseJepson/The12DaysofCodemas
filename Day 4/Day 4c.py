'''
Potentiometer to control LED flashes
'''

# Imports
from machine import Pin, ADC
import time

# Set LED Pins
red = Pin(20, Pin.OUT)
yellow = Pin(19, Pin.OUT)
green = Pin(18, Pin.OUT)

# Set Potentiometer Pins
potentiometer = ADC(Pin(27))

# Set LEDs to off
red.value(0)
yellow.value(0)
green.value(0)

while True:
    
    red.value(1)
    yellow.value(1)
    green.value(1)
    
    reading = potentiometer.read_u16() # take a reading from potentiometer
    flash_speed = reading/13000
    
    time.sleep(flash_speed)
    
    red.value(0)
    yellow.value(0)
    green.value(0)
    
    time.sleep(flash_speed)


'''
Potentiometer to turn LEDs on/off
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
    reading = potentiometer.read_u16() # take a reading from potentiometer
    
    print(reading) # print the reading
    
    if reading <= 20000:
        red.value(1)
        yellow.value(0)
        green.value(0)
    elif reading <= 40000:
        red.value(0)
        yellow.value(1)
        green.value(0)
    else:
        red.value(0)
        yellow.value(0)
        green.value(1)
    
    time.sleep(1)

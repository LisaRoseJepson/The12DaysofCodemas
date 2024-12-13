'''
Potentiometer to print readings
'''

# Imports
from machine import Pin, ADC
import time

# Set Potentiometer Pins
potentiometer = ADC(Pin(27))

while True:
    reading = potentiometer.read_u16() # take a reading from potentiometer
    
    print(reading) # print the reading
    
    time.sleep(1)
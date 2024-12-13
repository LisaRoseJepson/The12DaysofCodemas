'''
Break sensor - test
'''

# Imports
from machine import Pin
import time

# Set up sensor on GPIO26
breakbeam = Pin(26, Pin.IN, Pin.PULL_DOWN)

while True:
    
    time.sleep(0.1)
    
    if breakbeam.value() == 0:
        print("Beam broken!!!")
        

'''
Turn on board LED on (plus SOS signal!)
'''
# Imports
from machine import Pin
import time

# Set up Pin
onboardLED = Pin(25, Pin.OUT)
 
# Turn of LED
onboardLED.value(0)

# SOS
dash = 1
dot = 0.5

for i in range(3):
    onboardLED.value(1)
    time.sleep(dot)
    onboardLED.value(0)
    time.sleep(dot)
    
for i in range(3):
    onboardLED.value(1)
    time.sleep(dash)
    onboardLED.value(0)
    time.sleep(dot)
    
for i in range(3):
    onboardLED.value(1)
    time.sleep(dot)
    onboardLED.value(0)
    time.sleep(dot)
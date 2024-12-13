'''
Motion sensor - testing motion detection
'''

# Imports
from machine import Pin
import time

# Set up Pin for PIR sensor
pir = Pin(26, Pin.IN, Pin.PULL_DOWN)

# Wait 10 seconds for sensor to warm up
print("Sensor warming up...")
time.sleep(10)
print("Sensor ready!")

while True:
    
    time.sleep(0.1) # delay to prevent unnecessary program speed
    
    if pir.value() == 1: # if PIR detects movement
        print("I SEE YOU")
    
    time.sleep(5)
    
    print("Sensor active")
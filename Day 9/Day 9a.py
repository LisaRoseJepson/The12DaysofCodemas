'''
Tilt meter
'''

# Imports
from machine import Pin, PWM
import time

# Set up tilt sensor pin
tilt = Pin(26, Pin.IN, Pin.PULL_DOWN)

# Set up the Buzzer pin as PWM
buzzer = PWM(Pin(13)) # Set the buzzer to PWM mode

buzzer.duty_u16(0)
buzzer.freq(1000)

# Set LED Pins
red = Pin(20, Pin.OUT)
yellow = Pin(19, Pin.OUT)
green = Pin(18, Pin.OUT)

# Create a state variable at zero
state = 0

# Variable to count number of tilts
tiltcount = 0

while True:
    
    time.sleep(0.1)
    
    if state == 0 and tilt.value() == 1: # if titled
        print("Tilted")
        buzzer.duty_u16(5000)
        state = 1
        tiltcount += 1
        print(f"Tilt Count: {tiltcount}")
        red.value(1)
        green.value(0)
        
        time.sleep(0.5)
        buzzer.duty_u16(0)

    if state == 1 and tilt.value() == 0: # if stable
        print("Stable")
        state = 0
        green.value(1)
        red.value(0)
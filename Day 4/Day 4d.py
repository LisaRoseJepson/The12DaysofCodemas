'''
Potentiometer to control LED fading
'''

# Imports
from machine import Pin, ADC, PWM
import time

# Set up the LEDs for use with PWM
red = PWM(Pin(20))
yellow = PWM(Pin(19))
green = PWM(Pin(18))

# Set Potentiometer Pins
potentiometer = ADC(Pin(27))

# Set the PWM Freq - sets how often to switch power on and off for the LED
red.freq(1000)
yellow.freq(1000)
green.freq(1000)

# Set up reading variable
reading = 0

while True:
    
    reading = potentiometer.read_u16() # take a reading from potentiometer

    print(reading)

    # Set the LED PWM duty cycle to the potentiometer reading value
    # The duty cycle tells the LED for how long it should be on each time
    red.duty_u16(reading)
    yellow.duty_u16(reading)
    green.duty_u16(reading)
    
    time.sleep(0.001)
    
    



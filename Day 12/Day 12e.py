'''
Fading lights
'''

# Imports
import time
from machine import Pin, ADC
from neopixel import NeoPixel

# Define the strip pin number (28) and number of LEDs (15)
strand = NeoPixel(Pin(28), 15)

# Set up the potentiometer on ADC pin 26
potentiometer = ADC(Pin(26))

# Define our button pin
button = Pin(15, Pin.IN, Pin.PULL_DOWN)

# Colour variables
red = 255,0,0
green = 0,255,0
blue= 0,0,255

# Define colour list
colours = [red, green, blue]

# Set up delay
delay = 0.005

while True:
    
    for i in range(0, 255, 1):
        
        strand.fill((i, 0, 0))
        strand.write()
        
        time.sleep(delay)
        
    for i in range(255, 1, -1):
        
        strand.fill((i, 0, 0))
        strand.write()
        
        time.sleep(delay)       
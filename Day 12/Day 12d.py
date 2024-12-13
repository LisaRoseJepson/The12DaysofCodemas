'''
Lighting strip - changing colours, with button for changing colour
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

# Define variables for list indexing
indexlength = len(colours)-1
myindex = 0
state = 0

strand.fill((red))
strand.write()

while True: # Run forever

    if state == 0 and button.value() == 1: # if button is pressed
        
        myindex += 1
        
        if myindex > indexlength:
            myindex = 0
            
        state = 1
        
        strand.fill((colours[myindex]))
        
        strand.write()
        
        time.sleep(0.5)
        
    elif state == 1 and button.value() == 0:
        
        state = 0


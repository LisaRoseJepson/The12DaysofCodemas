'''
Light chaser - changing colours, with potentiometer for controlling speed
'''

# Imports
import time
from machine import Pin, ADC
from neopixel import NeoPixel

# Define the strip pin number (28) and number of LEDs (15)
strip = NeoPixel(Pin(28), 15)

# Set up the potentiometer on ADC pin 26
potentiometer = ADC(Pin(26))

# Colour variables
red = 255,0,0
green = 0,255,0
blue= 0,0,255

# Define colour list
colours = [red, green, blue]

while True: # Run forever

    # Iterate over the colours
    for j in colours:
        
        # Then iterate over 15 leds
        for i in range(15):
            
            delay = potentiometer.read_u16()/50000
            
            # Set each LED in the range to red
            strip[i] = (j)
            
            # Delay - the speed of the chaser
            time.sleep(delay)
            
            # Send the data to the strip
            strip.write()


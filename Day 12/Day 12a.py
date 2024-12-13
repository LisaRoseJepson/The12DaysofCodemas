'''
LED strip - lighting LEDs
'''

# Imports
from machine import Pin, ADC
from neopixel import NeoPixel
import time
import random

# Set up Pins
# Button
# Potentiometer

# LED details
num_leds = 15
GPIO_number = 28

# Define the LED pin number and number of LEDs
strand = NeoPixel(Pin(GPIO_number), num_leds)

# Set up colours
red = 255, 0, 0
green = 0,255,0
blue = 0,0,255
yellow = 255,255,0
pink = 255,20,147
off = 0, 0, 0

# colour list
colours = [red, green, blue, yellow, pink]

while True:
    
    #for led in range(num_leds):
    for colour in colours:
        
        #r = random.randint(0, 255)
        #g = random.randint(0, 255)
        #b = random.randint(0, 255)
        
        #strand[led] = (r, g, b)
        strand.fill((colour))
    
        strand.write()
        
        time.sleep(0.5)
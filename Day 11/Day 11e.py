'''
Display reading from light sensor
'''

# Imports
from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
import time

# Set up the button
button = Pin(8, Pin.IN, Pin.PULL_DOWN)

# Set up I2C and the pins we're using for it
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)

# Set up sensor GPIO as ADC Pin
lightsensor = ADC(Pin(26))

# Short delay to stop I2C falling over
time.sleep(1) 

# Define the display and size (128x32)
display = SSD1306_I2C(128, 32, i2c)

while True: # Loop forever
    
    time.sleep(1) 
    
    light = lightsensor.read_u16() # read in sensor value
    
    light_perc = round(light/65535*100, 1)
    
        
    display.fill(0) # Clear the display
    display.text("Light level", 0, 0) # Line 1
    display.text(str(light_perc) + "%",0,12) # Line 3
        
    display.show() # Update the display
        

'''
Simple text display
'''

# Imports
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

# Set up I2C and the pins we're using for it
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)

# Short delay to stop I2C falling over
time.sleep(1) 

# Define the display and size (128x32)
display = SSD1306_I2C(128, 32, i2c)

# Clear the display first
display.fill(0) 

# Write a line of text to the display
display.text("Merry Christmas!",0,0)
display.text("Happy New Year!",0,12) # (x, y) from top left corner
display.text("Lisa <3 James!",0,24)

# Update the display
display.show()
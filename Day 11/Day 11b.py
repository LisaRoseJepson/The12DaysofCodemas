'''
Endless counter
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

# Set up counter variable
count = 0

while True:
    
    time.sleep(0.5)
    
    count += 1
    
    display.fill(0)
    
    display.text("Endless counter: ", 0, 0)
    display.text(str(count), 64, 12)
    
    display.show()
    
    
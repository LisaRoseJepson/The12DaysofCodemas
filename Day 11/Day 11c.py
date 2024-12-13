'''
Naughty-Nice button
'''

# Imports
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

# Set up I2C and the pins we're using for it
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)

# Set up the button
button = Pin(8, Pin.IN, Pin.PULL_DOWN)

# Short delay to stop I2C falling over
time.sleep(1) 

# Define the display and size (128x32)
display = SSD1306_I2C(128, 32, i2c)

# Clear the display first
display.fill(0)

# Set up variables
state = 0
behaviour = ""

while True:
    
    time.sleep(0.1)
    
    display.fill(0)
    display.text("Naughty or Nice?", 0, 0)
    display.show()
    
    if state == 0 and button.value() == 1:
        
        state = 1
    
        if time.time() % 2 == 0:
            behaviour = "Nice"
        else:
            behaviour = "Naughty"

        # write behaviour to OLED  
        display.text(behaviour, 0, 12)
        display.show()
        
        time.sleep(1)
        display.fill(0) # clear display
        display.show()
    
    elif state == 1 and button.value() == 0:
        
        state = 0

    
    

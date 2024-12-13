'''
Reading from light sensor
Display LEDs for light level
Buzzer at low levels
'''

# Imports
from machine import Pin, ADC, PWM
from time import sleep

# Set up sensor GPIO as ADC Pin
lightsensor = ADC(Pin(26))

# Set LED Pins
red = Pin(20, Pin.OUT)
yellow = Pin(19, Pin.OUT)
green = Pin(18, Pin.OUT)

# Set up the Buzzer pin as PWM
buzzer = PWM(Pin(13)) # Set the buzzer to PWM mode

# Set LEDs to off
red.value(0)
yellow.value(0)
green.value(0)

while True:
    
    light = lightsensor.read_u16() # read in sensor value
    
    light_perc = round(light/65535*100, 2)

    print(f"Light {light_perc}%")
#    print(str(light_perc) +"%")

    if light_perc <= 33.3:
        red.value(1)
        buzzer.duty_u16(1000)
        buzzer.freq(500)    
        
    elif light_perc <= 66.7:
        yellow.value(1)
    else:
        green.value(1)
    
    sleep(1)

    # Set LEDs to off
    red.value(0)
    yellow.value(0)
    green.value(0)
    buzzer.duty_u16(0)

'''
Change buzzer volume with potentiometer
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

# Set up Buzzer Pin as PWM
buzzer = PWM(Pin(13))

# Set PWM duty
buzzer.duty_u16(10000)

# Set PWM freq to 1000 for 1 sec
buzzer.freq(1000)
time.sleep(1)

# Set PWM freq to 500 for 1 sec
buzzer.freq(500)
time.sleep(1)

# Turn buzzer off
buzzer.duty_u16(0)

volume = 0

while True:
    
    time.sleep(0.1)
    
    volume = potentiometer.read_u16() # read the volume
    
    print(volume)
    
    buzzer.freq(500) # set tone of buzzer
    buzzer.duty_u16(volume) # set the volume
    
    

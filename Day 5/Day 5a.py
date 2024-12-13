'''
Turn buzzer on, change tone, then off
'''

# Imports
from machine import Pin, ADC, PWM
import time

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


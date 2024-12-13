'''
TURN EFFIN BUZZER OFF!
'''

# Imports
from machine import Pin, PWM

# Set up Buzzer Pin as PWM
buzzer = PWM(Pin(13))

# Set PWM duty
buzzer.duty_u16(0)
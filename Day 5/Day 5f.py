'''
Play Jingle Bells with buzzer
'''

# Imports
from machine import Pin, PWM
import time

# Set up the Buzzer pin as PWM
buzzer = PWM(Pin(13)) # Set the buzzer to PWM mode

# Create our library of tone variables for "Jingle Bells"
C = 523
D = 587
E = 659
G = 784

# Create volume variable (Duty cycle)
volume = 10000

def note(note, volume, delay1, delay2):
    buzzer.duty_u16(volume)
    buzzer.freq(note)
    time.sleep(delay1)
    buzzer.duty_u16(0)
    time.sleep(delay2)   

note(E, volume, 0.1, 0.2)
note(E, volume, 0.1, 0.2)
note(E, volume, 0.1, 0.5)
note(E, volume, 0.1, 0.2)
note(E, volume, 0.1, 0.2)
note(E, volume, 0.1, 0.5)
note(E, volume, 0.1, 0.2)
note(G, volume, 0.1, 0.2)
note(C, volume, 0.1, 0.2)
note(D, volume, 0.1, 0.2)
note(E, volume, 0.1, 0.2)

buzzer.duty_u16(0)
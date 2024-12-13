'''
Beethoven's 9th
'''

# Imports
from machine import Pin, PWM
import time

# Set up the Buzzer pin as PWM
buzzer = PWM(Pin(13)) # Set the buzzer to PWM mode

# Create volume variable (Duty cycle)
volume = 10000

# Set LED Pins
red = Pin(20, Pin.OUT)
yellow = Pin(19, Pin.OUT)
green = Pin(18, Pin.OUT)

# Notes library
A = 440
As = 466
B = 494
C = 523
Cs = 554
D = 587
Ds = 622
E = 659
F = 698
Fs = 740
G = 784
Gs = 830

def note(note, volume, delay1, delay2):
    buzzer.duty_u16(volume)
    buzzer.freq(note)
    
    if note == E:
        red.value(1)
    elif note == C:
        red.value(1)
        yellow.value(1)
        green.value(1)
    elif note == D:
        yellow.value(1)
    else:
        green.value(1)
        
    time.sleep(delay1)
    buzzer.duty_u16(0)
    red.value(0)
    yellow.value(0)
    green.value(0)
    time.sleep(delay2)
    
note(B, volume, 0.1, 0.2)
note(B, volume, 0.1, 0.2)
note(C, volume, 0.1, 0.2)
note(D, volume, 0.1, 0.2)
note(D, volume, 0.1, 0.2)
note(C, volume, 0.1, 0.2)
note(B, volume, 0.1, 0.2)
note(A, volume, 0.1, 0.2)
note(G, volume, 0.1, 0.2)
note(G, volume, 0.1, 0.2)
note(A, volume, 0.1, 0.2)
note(B, volume, 0.1, 0.2)
note(B, volume, 0.1, 0.2)
note(A, volume, 0.1, 0.1)
note(A, volume, 0.1, 0.5)

buzzer.duty_u16(0)
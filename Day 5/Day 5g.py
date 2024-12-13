'''
Play Jingle Bells with buzzer AND LEDs WOOOH!!!
'''

# Imports
from machine import Pin, PWM
import time

# Set up the Buzzer pin as PWM
buzzer = PWM(Pin(13)) # Set the buzzer to PWM mode

# Create our library of tone variables for "Jingle Bells"
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

# Create volume variable (Duty cycle)
volume = 10000

# Set LED Pins
red = Pin(20, Pin.OUT)
yellow = Pin(19, Pin.OUT)
green = Pin(18, Pin.OUT)

def note(note, vol, delay1, delay2):
    buzzer.duty_u16(vol)
    buzzer.freq(note)
    
    if note == E:
        red.value(1)
    elif note == F:
        red.value(1)
        yellow.value(1)
        green.value(1)
    elif note == D:
        yellow.value(1)
    elif note == C:
        red.value(1)
        green.value(1)
    else:
        green.value(1)
        
    time.sleep(delay1)
    buzzer.duty_u16(0)
    red.value(0)
    yellow.value(0)
    green.value(0)
    time.sleep(delay2)

# Jingle Bells
note(E, volume, 0.1, 0.2)
note(E, volume, 0.1, 0.2)
note(E, volume, 0.1, 0.4)

# Jingle Bells
note(E, volume, 0.1, 0.2)
note(E, volume, 0.1, 0.2)
note(E, volume, 0.1, 0.4)

# Jingle all the way
note(E, volume, 0.1, 0.2)
note(G, volume, 0.1, 0.2)
note(C, volume, 0.1, 0.2)
note(D, volume, 0.1, 0.2)
note(E, volume, 0.1, 0.8)

# Oh what fun it is to ride
note(F, volume, 0.1, 0.2)
note(F, volume, 0.1, 0.2)
note(F, volume, 0.1, 0.2)
note(F, volume, 0.1, 0.2)
note(F, volume, 0.1, 0.2)
note(E, volume, 0.1, 0.2)
note(E, volume, 0.1, 0.2)

# on a one horse open sleigh
note(E, volume, 0.1, 0.1)
note(E, volume, 0.1, 0.1)
note(E, volume, 0.1, 0.2)
note(D, volume, 0.1, 0.2)
note(D, volume, 0.1, 0.2)
note(E, volume, 0.1, 0.2)
note(D, volume, 0.1, 0.4)
note(G, volume, 0.1, 0.4)

# Jingle Bells
note(E, volume, 0.1, 0.2)
note(E, volume, 0.1, 0.2)
note(E, volume, 0.1, 0.4)

# Jingle Bells
note(E, volume, 0.1, 0.2)
note(E, volume, 0.1, 0.2)
note(E, volume, 0.1, 0.4)

# Jingle all the way
note(E, volume, 0.1, 0.2)
note(G, volume, 0.1, 0.2)
note(C, volume, 0.1, 0.2)
note(D, volume, 0.1, 0.2)
note(E, volume, 0.1, 0.4)

# Oh what fun it is to ride
note(F, volume, 0.1, 0.2)
note(F, volume, 0.1, 0.2)
note(F, volume, 0.1, 0.2)
note(F, volume, 0.1, 0.2)
note(F, volume, 0.1, 0.2)
note(E, volume, 0.1, 0.2)
note(E, volume, 0.1, 0.2)

# on a one horse open sleigh
note(E, volume, 0.1, 0.1)
note(E, volume, 0.1, 0.1)
note(G, volume, 0.1, 0.2)
note(G, volume, 0.1, 0.2)
note(F, volume, 0.1, 0.2)
note(D, volume, 0.1, 0.2)
note(C, volume, 0.1, 0.8)

buzzer.duty_u16(0)

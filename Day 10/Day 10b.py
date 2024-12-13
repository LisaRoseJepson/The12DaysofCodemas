'''
Break sensor - game how many times can break beam in 30 secs
'''

# Imports
from machine import Pin, PWM
import time, sys

# Set up sensor on GPIO26
breakbeam = Pin(26, Pin.IN, Pin.PULL_DOWN)

# Set up the Buzzer pin as PWM
buzzer = PWM(Pin(13))

# Set LED Pins
red = Pin(20, Pin.OUT)
yellow = Pin(19, Pin.OUT)
green = Pin(18, Pin.OUT)

#  Set up variables
count = 0 # set up count to 0
buzzer.duty_u16(0) # turn buzzer off
buzzer.freq(1000) # Set buzzer PWM frequency to 1000
state = 0 # set state to zero
starttime = time.time() # snapshot of seconds since epoch (1-Jan-1970)
targetscore = 100 # set a target score for the game
red.value(0)
yellow.value(0)
green.value(0)

print("Game starts after the beep!")

#Long beep to signal game start
buzzer.duty_u16(10000)
time.sleep(2)
buzzer.duty_u16(0)

print("GO!")

while True:
    
    buzzer.duty_u16(0)
    
    time.sleep(0.0001)
    
    # Take the current epoch time and minus the start time
    # This gives us the number of seconds since we started the game
    timecheck = time.time() - starttime
  
    if timecheck >= 30:
        
        print(f"Your score is {count}. Well done!")
        sys.exit()
        
    elif state == 0 and breakbeam.value() == 0: # if beam broken
    
        buzzer.duty_u16(5000)
        count += 1
        state = 1 # set state to ensure beam unbroken again before increasing count again
        print("SCORE =", count) # Print our new score counter
        print("Time remaining:", (30 - timecheck)) # take our timecheck variable away from 30 - gives the remaining time
        
        if count <= targetscore*0.5:
            red.value(1)
        elif count <= targetscore*0.99:
            red.value(0)
            yellow.value(1)
        else:
            yellow.value(0)
            green.value(1)
        
    elif state == 1 and breakbeam.value() == 1: # checks if beam unbroken after a previous break
        
        state = 0
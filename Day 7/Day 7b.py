'''
Motion sensor - testing motion detection (with alarm)
'''

# Imports
from machine import Pin, PWM
import time

# Set up Pin for PIR sensor
pir = Pin(26, Pin.IN, Pin.PULL_DOWN)

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

# Set buzzer off
buzzer.duty_u16(0)

# Set volume
buzzer.freq(1000)

# Define alarm function
def alarm():
    
    print("I SEE YOU")
    
    for i in range(5):
        
        red.value(1)
        yellow.value(1)
        green.value(1)
        
        buzzer.duty_u16(5000)
        
        time.sleep(0.5)
        
        red.value(0)
        yellow.value(0)
        green.value(0)
        
        buzzer.duty_u16(500)
        
        time.sleep(0.5)
        
    buzzer.duty_u16(0)

# Wait 10 seconds for sensor to warm up
print("Sensor warming up...")
time.sleep(10)
print("Sensor ready!")

while True:
    
    time.sleep(0.1) # delay to prevent unnecessary program speed
    
    if pir.value() == 1: # if PIR detects movement
        alarm()
    
    time.sleep(5)
    
    print("Sensor active")

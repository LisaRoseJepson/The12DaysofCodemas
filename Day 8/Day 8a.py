'''
Take a temperature reading
'''

# imports
from machine import Pin, PWM
import time
import onewire
import ds18x20

# Set the data pin for the sensor
SensorPin = Pin(26, Pin.IN)

# Tell MicroPython we're using a DS18B20 sensor, and which pin it's on
sensor = ds18x20.DS18X20(onewire.OneWire(SensorPin))

# Look for DS18B20 sensors (each contains a unique rom code)
roms = sensor.scan()

# Set LED Pins
red = Pin(20, Pin.OUT)
yellow = Pin(19, Pin.OUT)
green = Pin(18, Pin.OUT)

# Set up the Buzzer pin as PWM
buzzer = PWM(Pin(13)) # Set the buzzer to PWM mode

buzzer.duty_u16(0)
buzzer.freq(1000)

while True:
      
    sensor.convert_temp() # Convert the sensor units to centigrade
 
    time.sleep(2) # Wait 2 seconds (you must wait at least 1 second before taking a reading)
    
    red.value(0)
    yellow.value(0)
    green.value(0)
    
    buzzer.duty_u16(0)
  
    for rom in roms:
        
        temp = (sensor.read_temp(rom))
        
        print(temp,"°C") # Print the temperature reading with °C after it
        
        if temp < 18:
            
            red.value(1)
            buzzer.duty_u16(5000)
            
        elif temp <= 22:
            
            yellow.value(1)
            
        else:
            
            green.value(1)
 
        time.sleep(5) # Wait 5 seconds before starting the loop again
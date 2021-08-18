## Part of this code was taken from the soil moisture sensor manual on joy-it.net https://joy-it.net/de/products/SEN-Moisture
from time import sleep
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as GPIO

def initialize():
    """Initialize the soil moisture sensor and the ADC module. Returns the chan0 object."""
    ## Create the I2C bus
    i2c = busio.I2C(board.SCL, board.SDA)
    ## Create the ADC object using the I2C bus
    ads = ADS.ADS1115(i2c)
    ## Create single-ended input on channel 0
    chan0 = AnalogIn(ads, ADS.P0)
    return chan0

def read_moisture(chan0):
    """Reads the voltage on the soil moisture sensor using chan0 as an argument."""
    try:
        while True:
            print("{:>5.3f}".format(chan0.voltage))
            sleep(5)
    except KeyboardInterrupt:
        GPIO.cleanup()

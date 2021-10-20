# This script interacts with the sensors; it reads the values and stores them into a numpy array.

import pandas as pd
from pigpio_dht import DHT22
import time, datetime
import matplotlib.pyplot as plt

csv_path = "/home/pi/KiraPi/output/sens.txt" # Where the measurements will be stored
# Create pandas DataFrame
df = pd.DataFrame(columns=['time', 'temp_c', 'temp_f', 'humidity', 'valid'])
# Set the dtype of the time column to datetime64[ns]
df['time'] = pd.to_datetime(df['time'])
def dht_init(gpio):
    """
    Initialize the DHT22 sensor and return it
    
    :param int gpio: The GPIO BCM pin number where the sensor is attached
    """
    try:
        dht_sensor = DHT22(gpio) # Create the DHT22 object with the corresponding GPIO pin number
        print("DHT22 sensor initialized.")
        return dht_sensor,df # Return the sensor object and the empty dataframe
    except:
        print("DHT22 sensor could not be initialized.")

def dht_reader(dht_sensor):
    """
    Return DHT22 sensor measurements in dictionary with time of measurement

    :param dht_sensor: The initialized dht_sensor object
    :return: the measured data as a dictionary
    :rtype: dict
    """
    try:
        data = dht_sensor.read(retries=1) # Try to read the DHT22 sensor values and store as dictionary.
    except TimeoutError: # If a TimeoutError arises, write all zeros and classify as invalid.
        data = {'temp_c': 0, 'temp_f': 0, 'humidity': 0, 'valid': False}
    data["time"] = time.mktime(datetime.datetime.now().timetuple()) # Write the time of measurement
    return data

def dht_logger(dht_sensor):
    """
    Reads DHT22 sensor values, writes them to a file and returns them as a numpy array

    :param dht_sensor: The initialized dht_sensor object
    """
    data = dht_reader(dht_sensor)
    df_append = pd.DataFrame(data_list, columns = ['Sensor', 'Value'])
    df = dht_df.append
    df.to_csv(csv_path, header=None, index=None, sep=' ', mode='a')

# Loops through a set of DHT22 measurements and adds the data to the received dataframe. Then appends to the csv file.
def dht22_multi_measure(dht_sensor, df, ran): # takes the dht_sensor object, df dataframe and the number of planned measurements as arguments
    """
    Do a loop over a set of measurements
    
    :param dht_sensor: The dht_sensor object
    :param df df: The dataframe to add the measurments into
    :param int ran: The Number of measurements
    """
    try:
        #Loop through the received number of iterations
        for i in range(ran):
            # Measures, append to the dataframe and writes the value to the csv file.
            df.append(dht_reader(dht_sensor), ignore_index=True).to_csv(csv_path, header=None, index=None, sep=' ', mode='a')
            # Wait before the next measurement, so as not to create TimeoutErrors
            time.sleep(1)
    except:
        print("An error has occured.")

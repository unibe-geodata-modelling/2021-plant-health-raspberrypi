# This script interacts with the sensors; it reads the values and stores them into a numpy array.

import pandas as pd
from pigpio_dht import DHT22
import time, datetime
import matplotlib.pyplot as plt
import csv

csv_path = "/home/pi/KiraPi/output/sens.txt" # Where the measurements will be stored
columns=['date', 'time', 'temp_c', 'temp_f', 'humidity', 'valid'] # The columns titles

def dht_init(gpio):
    """
    Initialize the DHT22 sensor and return it
    
    :param int gpio: The GPIO BCM pin number where the sensor is attached
    :return dht_sensor: The initialized dht_sensor object
    :return df: The initialized DataFrame
    """
    try:
        # Create pandas DataFrame
        df = pd.DataFrame(columns=columns)
        # Set the dtype of the time column to datetime64[ns] to have an interchangeable unit
        df['date'] = pd.to_datetime(df['date'])
        df['time'] = pd.to_datetime(df['time'])
        # Create the DHT22 object with the corresponding GPIO pin number
        dht_sensor = DHT22(gpio) 
        # Create a CSV file with given columns names
        with open(csv_path, 'w', newline='') as file:
            writer = csv.writer(file, delimiter=' ') # The separator is a single space
            writer.writerow(columns) # Write the header row
            file.close()
        print("DHT22 sensor initialized.")
        return dht_sensor,df # Return the sensor object and the empty dataframe
    except:
        print("DHT22 sensor could not be initialized.")

def dht_reader(dht_sensor):
    """
    Return DHT22 sensor measurements in dictionary with time of measurement

    :param dht_sensor: The initialized dht_sensor object
    :return dict data: the measured data as a dictionary
    """
    try:
        # Try to read the DHT22 sensor values and store as dictionary.
        data = dht_sensor.read(retries=1)
    except TimeoutError: # If a TimeoutError arises, write all zeros and classify as invalid.
        data = {'temp_c': 0, 'temp_f': 0, 'humidity': 0, 'valid': False}
    meas_datetime = datetime.datetime.now()
    data['date'] = meas_datetime.date()
    data['time'] = meas_datetime.time() # Write the time of measurement
    return data

##def dht_logger(dht_sensor):
##    """
##    Reads DHT22 sensor values, writes them to a file and returns them as a numpy array
##
##    :param dht_sensor: The initialized dht_sensor object
##    """
##    data = dht_reader(dht_sensor)
##    df_append = pd.DataFrame(data_list, columns = ['Sensor', 'Value'])
##    df = dht_df.append
##    df.to_csv(csv_path, header=None, index=None, sep=' ', mode='a')

# Loops through a set of DHT22 measurements and adds the data to the received dataframe. Then appends to the csv file.
def dht22_multi_measure(dht_sensor, df, ran): # takes the dht_sensor object, df dataframe and the number of planned measurements as arguments
    """
    Do a loop over a set of measurements, write to csv and DataFrame and return the latter
    
    :param dht_sensor: The dht_sensor object
    :param df df: The dataframe to add the measurements into
    :param int ran: The Number of measurements
    :return df df: the appended DataFrame
    """
    try:
        #Loop through the received number of iterations
        for i in range(ran):
            # Measures, appends to the dataframe and writes the value to the csv file.
            measurement = dht_reader(dht_sensor)
            df = df.append(measurement, ignore_index=True)
            # Wait before the next measurement, so as not to create too many TimeoutErrors
            time.sleep(1)
        df.to_csv (csv_path, index = False, header=None, sep=' ', mode='a')
        return df
    except:
        print("An error has occured during the batch measurement.")

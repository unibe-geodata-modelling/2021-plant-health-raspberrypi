# This script interacts with the sensors; it reads the values and stores them into a numpy array.

import pandas as pd
from pigpio_dht import DHT22
import time, datetime
gpio = 4 # BCM Numbering
dht_sensor = DHT22(gpio) # Create the DHT22 object with the corresponding GPIO pin number

csv_path = "/home/pi/KiraPi/sens.txt"
# Create pandas DataFrame
df = pd.DataFrame(columns=['time', 'temp_c', 'temp_f', 'humidity', 'valid'])
# Set the dtype of the time column to datetime64[ns]
df['time'] = pd.to_datetime(df['time'])


def dht_reader():
    """Return DHT22 sensor measurements in dictionary with time of measurement."""
    try:
        data = dht_sensor.read(retries=1) # Try to read the DHT22 sensor values and store as dictionary.
    except TimeoutError: # If a TimeoutError arises, write all zeros and classify as invalid.
        data = {'temp_c': 0, 'temp_f': 0, 'humidity': 0, 'valid': False}
    data["time"] = time.mktime(datetime.datetime.now().timetuple()) # Set the time of measurement
    return data

##def dht_logger(dht_df):
##    """Reads DHT22 sensor values, writes them to a file and returns them as a numpy array."""
##    data = dht_reader()
##    df_append = pd.DataFrame(data_list, columns = ['Sensor', 'Value'])
##    df = dht_df.append

# Loops through a set of DHT22 measurements and adds the data to the DF
for i in range(20):
    df = df.append(dht_reader(), ignore_index=True)
    time.sleep(1)
    df.to_csv(csv_path, header=None, index=None, sep=' ', mode='a')

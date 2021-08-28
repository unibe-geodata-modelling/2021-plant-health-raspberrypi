# This script interacts with the sensors; it reads the values and stores them into a numpy array.

import pandas as pd
from pigpio_dht import DHT22
import time, datetime
gpio = 4 # BCM Numbering
dht_sensor = DHT22(gpio) # Create the DHT22 object with the corresponding GPIO pin number

# Create pandas DataFrame
df = pd.DataFrame(columns=['time', 'temp_c', 'temp_f', 'humidity', 'valid'])
# Set the dtype of the time column to datetime64[ns]
df['time'] = pd.to_datetime(df['time'])


def dht_reader():
    """Return DHT22 sensor measurements in dictionary with time of measurement."""
    data = dht_sensor.read() # Read the DHT22 sensor values and store as dictionary
    data["time"] = time.mktime(datetime.datetime.now().timetuple()) # Set the time of measurement
    return data

##def dht_logger(dht_df):
##    """Reads DHT22 sensor values, writes them to a file and returns them as a numpy array."""
##    data = dht_reader()
##    df_append = pd.DataFrame(data_list, columns = ['Sensor', 'Value'])
##    df = dht_df.append

# Loops through a set of DHT22 measurements and adds the data to the DF
for i in range(10):
    df = df.append(dht_reader(), ignore_index=True)
    time.sleep(3)
print(df)

# This is the main script to run the KiraPi workflow.

import moisture
import datetime
import dht22
import plotter

gpio = 4 # BCM Numbering

##chan0 = moisture.initialize()
##moisture.read_moisture(chan0)

# Initialize the dht22 sensor. Pass the gpio number and get the sensor object and the dataframe.
dht_sensor,df = dht22.dht_init(gpio)
##print(dht22.dht_reader(dht_sensor))
#print (datetime.datetime.now())
##dht22.dht22_multi_measure(dht_sensor,df, 2)

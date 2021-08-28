# This is the main script to run the KiraPi workflow.

import moisture
import datetime
import dht22

gpio = 4 # BCM Numbering

chan0 = moisture.initialize()
##moisture.read_moisture(chan0)
dht_sensor = dht22.dht_init(gpio)
#print (datetime.datetime.now())

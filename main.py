# This is the main script to run the KiraPi workflow.
import moisture
import datetime
chan0 = moisture.initialize()
moisture.read_moisture(chan0)
#print (datetime.datetime.now())

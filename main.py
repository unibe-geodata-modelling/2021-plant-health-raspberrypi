# This is the main script to run the KiraPi workflow.
import moisture
chan0 = moisture.initialize()
moisture.read_moisture(chan0)

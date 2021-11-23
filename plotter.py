import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

## Paths
csv_path = "/home/pi/KiraPi/output/sens.txt"
## Plotter function
def plotter():
    """
    Read the values from a csv file and plot them
    """
    try:
        ## Read the csv file into a dataframe.
        # The separator is defined with sep and can be written in Regex.
        df = pd.read_csv(csv_path, sep='\s+')
        df['time'] = pd.to_datetime(df['time'])
        # Drop invalid measurements
        df = df[df.valid != False]
        
        ## Print info on the Dataframe
        #print(df)
        #df.info()
        ## Create figure and plot space
        fig, ax1 = plt.subplots(figsize=(10, 10))

        ## Add x-axis and y-axis
        ax1.scatter(df['time'],
                   df['temp_c'],
                   color='purple')

        ## Set title and labels for axes
        ax1.set(xlabel="Time",
               ylabel='Temp (°C)',
               title="Temperature Plot")
        #Set the temperature range and tick distance to plot the y axis
        start, end = 18,25
        ax1.set_ylim([start,end])
        ax1.yaxis.set_ticks(np.arange(start, end, 1))

        plt.scatter(df['time'],
                    df["temp_c"])

        ## Adding Twin Axes
        ax2 = ax1.twinx()
        ax2.set_ylabel("Air Humidity (%)")
        ax2.set_ylim([40,100])
        
        ax2.scatter(df['time'],
                    df["humidity"],
                    color = 'red')

        ## Set the time range and tick distance to plot the x axis
        # Use this if you want to change the distance between the time ticks.
        #start , end = ax1.get_xlim()
        #ax1.xaxis.set_ticks(np.arange(start, end, 0.001))

        ## Rotate and align the tick labels so they look better
        fig.autofmt_xdate()
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

        ## Save the plot to file
        fig.savefig("/home/pi/KiraPi/output/figure.png")
        ## Show the plot
        plt.show()
    except:
        df.info()
        print("An error has occured.")

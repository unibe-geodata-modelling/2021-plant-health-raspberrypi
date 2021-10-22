import pandas as pd
##import time, datetime
import matplotlib.pyplot as plt

def plotter(csv_path):
    """
    Read the values from a csv file and plot them

    :param csv_path: Path to the csv file to plot
    """
    try:
        # Read the csv file into a dataframe. The separator is defined with sep and can be written in Regex.
        df = pd.read_csv(csv_path, sep='\s+')
        df['time'] = pd.to_datetime(df['time'])
    
##        plt.plot(df, x="time", y="temp_c", kind="scatter")
        df.info()
        # Create figure and plot space
        fig, ax = plt.subplots(figsize=(10, 10))

        # Add x-axis and y-axis
        ax.scatter(df.index.values,
                   df['temp_c'],
                   color='purple')

        # Set title and labels for axes
        ax.set(xlabel="Time",
               ylabel="Temp C",
               title="Temperature Plot")
##        plt.scatter(df["temp_c"])
        plt.show()
    except:
        df.info()
        print("An error has occured.")

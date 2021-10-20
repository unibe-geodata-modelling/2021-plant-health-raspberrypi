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
        df = pd.read_csv(csv_path, sep='\s+', usecols=["temp_c"])
        plt.plot(df)
        plt.show()
    except:
        print("An error has occured.")

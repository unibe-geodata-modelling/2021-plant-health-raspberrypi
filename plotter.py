import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

## Plotter function
def plotter(csv_path):
    """
    Read the values from a csv file and plot them

    :param csv_path: Path to the csv file to plot
    """
    try:
        ## Read the csv file into a dataframe.
        # The separator is defined with sep and can be written in Regex.
        df = pd.read_csv(csv_path, sep='\s+')
        df['time'] = pd.to_datetime(df['time'])
        # Drop invalid measurements
        df = df[df.valid != False]
    
##        plt.plot(df, x="time", y="temp_c", kind="scatter")
        
        ## Print info on the Dataframe
        print(df)
        df.info()
        ## Create figure and plot space
        fig, ax = plt.subplots(figsize=(10, 10))

        ## Add x-axis and y-axis
        ax.scatter(df['time'],
                   df['temp_c'],
                   color='purple')

        ## Set title and labels for axes
        ax.set(xlabel="Time",
               ylabel='Temp (°C)',
               title="Temperature Plot")
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
        plt.scatter(df['time'],
                    df["temp_c"])

        ## rotate and align the tick labels so they look better
        fig.autofmt_xdate()
##        dates = dt.dates.date2num(df['time'])
##        plt.plot_date(dates, values)

        ## Save the plot to file
        fig.savefig("/home/pi/KiraPi/output/figure.png")
        ## Show the plot
        plt.show()
    except:
        df.info()
        print("An error has occured.")

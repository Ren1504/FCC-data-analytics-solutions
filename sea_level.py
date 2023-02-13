import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file

    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x,y = df['Year'], df['CSIRO Adjusted Sea Level']

    plt.scatter(x,y)

    # Create first line of best fit

    linear = linregress(x,y)
    years = np.array(range(1880,2051))
    y1 = (linear.slope * years) +linear.intercept

    # Create second line of best fit

    new_df = df.loc[df['Year'] >= 2000]
    x_new,y_new = new_df['Year'], new_df['CSIRO Adjusted Sea Level']
    linear2 = linregress(x_new,y_new)
    years2 = np.array(range(2000,2051))
    y2 = (linear2.slope * years2) +linear2.intercept



    # Add labels and title

    plt.plot(years,y1,color = 'b')
    plt.plot(years2,y2,color = 'r')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()



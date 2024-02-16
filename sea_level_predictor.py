import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    res1 = linregress(y=df['CSIRO Adjusted Sea Level'],x=df['Year'])
    plt.plot(range(1880,2051,1), res1.intercept + res1.slope*range(1880,2051,1), 'r')
    # Create second line of best fit
    res2 = linregress(df.loc[df['Year']>=2000,'Year'], df.loc[df['Year']>=2000,'CSIRO Adjusted Sea Level'])
    plt.plot(range(2000,2051,1), res2.intercept + res2.slope*range(2000,2051,1), 'y')
    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
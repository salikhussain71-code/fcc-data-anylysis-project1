import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Line of best fit for all data
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = np.arange(df['Year'].min(), 2051)
    y_pred = res.slope * x_pred + res.intercept
    ax.plot(x_pred, y_pred, 'r', label='Best fit line 1880-2050')
    
    # Line of best fit from 2000 onwards
    df_2000 = df[df['Year'] >= 2000]
    res2 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x_pred2 = np.arange(2000, 2051)
    y_pred2 = res2.slope * x_pred2 + res2.intercept
    ax.plot(x_pred2, y_pred2, 'g', label='Best fit line 2000-2050')
    
    # Labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()
    
    # Save plot
    plt.savefig('sea_level_plot.png')
    return plt.gcf()

# Test it
draw_plot()
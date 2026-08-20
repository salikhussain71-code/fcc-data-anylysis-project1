import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['BMI'] = df['weight'] / (df['height'] / 100) ** 2
df['overweight'] = (df['BMI'] > 25).astype(int)
df = df.drop('BMI', axis=1)

# Normalize data
df[['cholesterol', 'gluc']] = df[['cholesterol', 'gluc']].apply(lambda x: (x > 1).astype(int))

def draw_cat_plot():
    # Create DataFrame for cat plot
    df_cat = pd.melt(df, id_vars=['cardio'], 
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    
    # Group and reformat
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    
    # Draw catplot
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio',
                      data=df_cat, kind='bar').fig
    
    fig.savefig('catplot.png')
    return fig

def draw_heat_map():
    # Clean data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]
    
    # Calculate correlation matrix
    corr = df_heat.corr()
    
    # Generate mask for upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    # Set up matplotlib figure
    fig, ax = plt.subplots(figsize=(11, 9))
    
    # Plot heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})
    
    fig.savefig('heatmap.png')
    return fig

# Test it
draw_cat_plot()
draw_heat_map()
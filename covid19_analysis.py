# COVID-19 Data Analysis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("../data/owid-covid-data.csv")

# Clean and inspect data
df = df[df['iso_code'].str.startswith('OWID') == False]
df['date'] = pd.to_datetime(df['date'])
df.fillna(0, inplace=True)

# Global trend of cases
global_data = df.groupby('date')[['new_cases', 'new_deaths', 'new_vaccinations']].sum()

plt.figure(figsize=(14, 6))
plt.plot(global_data.index, global_data['new_cases'], label='New Cases')
plt.plot(global_data.index, global_data['new_deaths'], label='New Deaths')
plt.title('Global Daily COVID-19 Cases and Deaths')
plt.xlabel('Date')
plt.ylabel('Count')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Top 10 countries by total deaths
latest_date = df['date'].max()
latest_data = df[df['date'] == latest_date]
top_deaths = latest_data[['location', 'total_deaths']].sort_values(by='total_deaths', ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(data=top_deaths, x='total_deaths', y='location', palette='Reds_r')
plt.title('Top 10 Countries by Total COVID-19 Deaths')
plt.xlabel('Total Deaths')
plt.ylabel('Country')
plt.tight_layout()
plt.show()

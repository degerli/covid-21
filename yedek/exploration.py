import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data.csv')

# Convert date from YYYY.MM.DD to YYYY-MM-DD
df['Date'] = df['Date'].str.replace('.', '-')

# Plot figure
plt.plot(df['Date'], df['China_With'], '.b')
plt.xticks(df['Date'].values[::2], rotation=20)
plt.show()

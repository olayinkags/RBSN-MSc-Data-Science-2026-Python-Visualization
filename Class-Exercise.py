# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# File location
# fileURL = "https://github.com/IbrahimHammed/RBSN-MSc-Data-Science-2026-Python-Visualization/blob/main/sp500.csv?raw=true"
fileURL = "https://raw.githubusercontent.com/IbrahimHammed/RBSN-MSc-Data-Science-2026-Python-Visualization/refs/heads/main/sp500.csv"

# Read data into a dataframe
df = pd.read_csv(fileURL)
dfSampleRows = df.head(10)

# Display the sample rows dataframe
dfSampleRows

# Visualization
fig, ax  = plt.subplots(figsize=(10,6))

# fig.set(figheight=6, figwidth=10)

# Series 1
ax.plot(dfSampleRows['Date'], dfSampleRows['Volume'], linestyle='-.', linewidth=3, marker='^', markersize=10, markeredgewidth=2, markerfacecolor='orange', markeredgecolor='red', label='Series-1')

# Series 2
ax.plot(dfSampleRows['Date'], dfSampleRows['Volume'] * 0.5, linestyle='--', linewidth=3, marker='o', markersize=10, markeredgewidth=2, markerfacecolor='orange', markeredgecolor='red', label='Series-2')

ax.set_title("S&P 500 Volume over 10 days", fontsize=16, fontweight='bold', color="red", loc='center')
ax.set_xlabel("Trade Date", fontsize=12)
ax.set_ylabel("Volume", fontsize=12)

# Rotate x-axis labels
plt.xticks(rotation=45)

# Style the chart area
ax.set_facecolor('#1e1e1e')

# Gridlines: Major
ax.grid(which='major', color='#666666', linestyle='-')

# Gridlines: Minor
ax.grid(which='minor', color='#999999', linestyle='-', alpha=0.2)
ax.minorticks_on()

# Legend
ax.legend(loc='upper left', facecolor='#ffffff', fontsize=10, title='10d Market Movement')

plt.show()

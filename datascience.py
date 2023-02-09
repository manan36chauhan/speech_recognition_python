import pandas as pd

# Load data into a dataframe
df = pd.read_csv('data.csv')

# Get basic statistics of the data
print(df.describe())

# Get the column-wise mean of the data
print(df.mean())

# Get the correlation between different columns
print(df.corr())

# Plot a histogram of a column
import matplotlib.pyplot as plt
plt.hist(df['column_name'])
plt.show()
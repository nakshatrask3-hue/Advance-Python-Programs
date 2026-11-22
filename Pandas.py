
import pandas as pd
import numpy as np

# Creating a Series with 10 random numbers
data = np.random.randint(1, 100, 10)
series = pd.Series(data)

print("Original Series:")
print(series)

# Indexing
print("\nElement at index 3:")
print(series[3])

# Filtering
print("\nNumbers greater than 50:")
print(series[series > 50])

# Statistical Operations
print("\nMean:", series.mean())
print("Median:", series.median())
print("Minimum:", series.min())
print("Maximum:", series.max())

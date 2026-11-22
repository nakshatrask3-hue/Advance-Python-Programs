
import numpy as np

# Creating a one-dimensional array
arr = np.arange(1, 11)

print("Original Array:")
print(arr)

# Slicing operations
print("\nFirst five elements:")
print(arr[:5])

print("\nLast five elements:")
print(arr[5:])

print("\nElements from index 2 to 6:")
print(arr[2:7])

# Statistical operations
print("\nSum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# Broadcasting operation
arr = arr + 5

print("\nArray after adding 5 using broadcasting:")
print(arr)

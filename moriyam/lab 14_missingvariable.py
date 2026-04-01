import numpy as np

arr = np.array([1, 2, np.nan, 4])

np.isnan(arr)


arr[np.isnan(arr)] = np.nanmean(arr)

print(arr)

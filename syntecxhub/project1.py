import numpy as np
import pandas as pd
import time

print("===== NumPy Data Explorer =====")

print('Array Creation\n')
arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)
print("\nMatrix Creation\n")
matrix = np.arange(1, 11).reshape(5,2)
print("Matrix:\n", matrix)
print("\nLoading Data from CSV\n")
data=pd.read_csv('data.csv')
print("Data from CSV:\n", data.head(10))

print('\n\nIndexing\n')
print("\nFirst element of array:", arr[0])
print("Last element of array:", arr[-1])
print("Second row of matrix:", matrix[1])
print("Element at (1,1) in matrix:", matrix[1,1])
print("First 3 rows of data:\n", data.iloc[:3])
print("First 3 rows of first column in data:\n", data.iloc[:3, 0])
print("Last 2 rows of data:\n", data.iloc[-2:])

print('\n\nSlicing\n')
print("\nArray slice (0:3):", arr[0:3])
print("Matrix slice (rows 1-3, all columns):\n", matrix[1:4, :])
print("Data slice (first 5 rows, columns 0-2):\n", data.iloc[:5, :3])

print('\n\nMathematical Operations\n')
print("\nAdd 5 to each element:", arr + 5)
print("Element-wise multiplication:", arr * 2)
print("Square root of each element:", np.sqrt(arr))
print("Matrix multiplication:\n", np.dot(matrix.T, matrix))
print("Addition of first column elements of data:\n", data.iloc[:, 0].sum())

print('\n\nAxis-wise Operations\n')
print("\nArray sum:", arr.sum())
print("Array mean:", arr.mean())
print("\nMatrix row-wise sum:", matrix.sum(axis=1))
print("Matrix column-wise mean:", matrix.mean(axis=0))
print("\nData column-wise sum:\n", data.sum(axis=0))
print("Data column-wise mean:\n", data.mean(axis=0))

print('\n\nStatistical Functions\n')
print("\nMax:", np.max(arr))
print("Min:", np.min(arr))
print("Standard Deviation:", np.std(arr))
print("\nMatrix Max (axis=0):", np.max(matrix, axis=0))
print("Matrix Min (axis=1):", np.min(matrix, axis=1))
print("\nData Max (axis=0):\n", data.max(axis=0))
print("Data Min (axis=0):\n", data.min(axis=0))


print('\n\nReshaping & Broadcasting\n')
reshaped = arr.reshape(5, 1)
print("\nReshaped Array (5x1):\n", reshaped)

broadcasted = matrix + np.array([1, 2])
print("\nBroadcasted Matrix:\n", broadcasted)

print('\n\nSaving & Loading Data\n')
np.save("my_array.npy", arr)
loaded_arr = np.load("my_array.npy")
print("\nLoaded Array from file:", loaded_arr)

print('\n\nNumPy vs Python List Performance')
nums = list(range(1_000_000))
np_nums = np.arange(1_000_000)

# Python list performance
start = time.time()
python_result = [x * 2 for x in nums]
python_time = time.time() - start

# NumPy performance
start = time.time()
numpy_result = np_nums * 2
numpy_time = time.time() - start

print("\nPython List Time:", python_time)
print("NumPy Time:", numpy_time)
print("NumPy is faster by:", python_time / numpy_time, "times")
"""
    Numpy

    Basics:
        It provides a high performance multidimensional array object, and tools for working with these arrays

    [1]. It provides option as:
    [2]. Less Memory optimized
    [3]. Fast performance
    [4]. Convenient and easy to use

"""
import numpy as np
import matplotlib.pyplot as plt

arr = np.array([(1, 2, 3, 4, 5), (4, 5, 6, 7, 8)])

# Find dimension of an array
print("Dimension:", arr.ndim)

# Find byte size of each element
print("Byte size:", arr.itemsize)

# Find data type of each element
print("Data type:", arr.dtype)

# Array size
print("Array size:", arr.size)

# Array shape (Cols * Rows)
print("Array shape:", arr.shape)

# Re Array shape
arr = arr.reshape(5, 2)
print("Re Array shape:", arr.shape)
arr = arr.reshape(2, 5)

# Slicing array
arr = np.array([('R1C1', 'R1C2', 'R1C3', 'R1C4', 'R1C5'),
                ('R2C1', 'R2C2', 'R2C3', 'R2C4', 'R2C5'),
                ('R3C1', 'R3C2', 'R3C3', 'R3C4', 'R3C5'),
                ('R4C1', 'R4C2', 'R4C3', 'R4C4', 'R4C5')])

print(arr[0:8, :0])

# array operations
arr1 = np.array([(11, 12, 13), (14, 15, 16), (17, 18, 19)])
arr2 = np.array([(21, 22, 23), (24, 25, 26), (27, 28, 29)])

# array sum
print(arr1 + arr2)

# array mul
print(arr1 * arr2)

# array sub
print(arr2 - arr1)

# print mod
print(arr1 / arr2)

# square root
print(np.sqrt(arr1))

# standard deviation
print(np.std(arr1))


# Special functions
arrX = np.arange(0, 3*np.pi, 0.1)
arrSin = np.sin(arrX)
plt.plot(arrX, arrSin)
plt.show()

# Cosine
arrCos = np.cos(arrX)
plt.plot(arrX, arrCos)
plt.show()

# tan ...
arrTan = np.tan(arrX)
plt.plot(arrX, arrTan)
plt.show()

arrSpec = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])

# Exponential
print(np.exp(arrSpec))

# log module
print(np.log(arrSpec))

# Advanced
ar = np.arange(12).reshape(3, 4)
print(ar)

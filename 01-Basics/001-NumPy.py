# What is NumPy?¶
#
# NumPy is the fundamental package for scientific computing in Python.
# It is a Python library that provides a multidimensional array object,
# various derived objects (such as masked arrays and matrices),
# and an assortment of routines for fast operations on arrays, including mathematical,
# logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms,
# basic linear algebra, basic statistical operations, random simulation and much more.

import numpy as np

l = [1, 2, 3]

print(np.array(l))
# [1 2 3]

print(type(np.array(l)))
# <class 'numpy.ndarray'>

print(np.arange(0, 10))
# [0 1 2 3 4 5 6 7 8 9]

print(np.arange(0, 10, 3))
# [0 3 6 9]

print('=============================================')

# Ref
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.zeros.html

print(np.zeros(5))
# [ 0.  0.  0.  0.  0.]

print(np.zeros((2, 3)))
# 2 rows and 3 cols
# [[ 0.  0.  0.]
# [ 0.  0.  0.]]

print('=============================================')

# Ref
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.ones.html

print(np.ones(2))
# [ 1.  1.]

print(np.ones((2, 4)))
# [[ 1.  1.  1.  1.]
# [ 1.  1.  1.  1.]]

print('=============================================')

# Ref
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html

print(np.linspace(1, 100, 5))
# [   1.     25.75   50.5    75.25  100.  ]

print('=============================================')

# Ref
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.randint.html

print(np.random.randint(1, 100))
# some random number between 1 to 100

print(np.random.randint(1, 100, (2, 3)))
# array of random number 2 rows and 3 cols
# [[61  4  5]
#  [ 1 59 21]]

print('=============================================')

# Ref
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.seed.html

np.random.seed(101)
print(np.random.randint(1, 10))
# 2
print(np.random.randint(1, 10))
# 7

print('=============================================')

np.random.seed(101)
arr = np.random.randint(1, 10, 10)

print(arr)  # [2 7 8 9 5 9 6 1 6 9]
print(arr.max())  # 9
print(arr.argmax())  # index location of max value 3
print(arr.min())  # 1
print(arr.mean())  # 6.2
print(arr.reshape(2, 5))
# 2row 3col
# [[2 7 8 9 5]
#  [9 6 1 6 9]]

print('=============================================')

mat = np.arange(0, 100).reshape(10, 10)
print(mat)
# [[ 0  1  2  3  4  5  6  7  8  9]
#  [10 11 12 13 14 15 16 17 18 19]
#  [20 21 22 23 24 25 26 27 28 29]
#  [30 31 32 33 34 35 36 37 38 39]
#  [40 41 42 43 44 45 46 47 48 49]
#  [50 51 52 53 54 55 56 57 58 59]
#  [60 61 62 63 64 65 66 67 68 69]
#  [70 71 72 73 74 75 76 77 78 79]
#  [80 81 82 83 84 85 86 87 88 89]
#  [90 91 92 93 94 95 96 97 98 99]]

print(mat[5, 5])  # 55
# slicing
print(mat[:, 0])  # [ 0 10 20 30 40 50 60 70 80 90]
print(mat[1, :])  # [10 11 12 13 14 15 16 17 18 19]
print(mat[0:3, 0:3])
# [[ 0  1  2]
#  [10 11 12]
#  [20 21 22]]

print('=============================================')

# masking


print(mat > 50)
# [[False False False False False False False False False False]
#  [False False False False False False False False False False]
#  [False False False False False False False False False False]
#  [False False False False False False False False False False]
#  [False False False False False False False False False False]
#  [False  True  True  True  True  True  True  True  True  True]
#  [ True  True  True  True  True  True  True  True  True  True]
#  [ True  True  True  True  True  True  True  True  True  True]
#  [ True  True  True  True  True  True  True  True  True  True]
#  [ True  True  True  True  True  True  True  True  True  True]]
print(mat[mat > 50])
# [51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75
#  76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99]

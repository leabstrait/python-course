#Normal way
matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(matrix)
matrix[0][1]

# What if we wanted to multiply every element in the matrix by 2
[[elem*2 for elem in sublist] for sublist in matrix]

# Using numpy
from numpy import array

matrix = array([[1,2,3], [4,5,6], [7,8,9]])
print(matrix)
matrix[0][1]
matrix[0,1]

# Now we can do scalar multiplication
print(matrix * 2)

# Matrix arithmetic
secondMatrix = array([[5,4,3], [7,6,5], [9,8,7]])
print(secondMatrix - matrix)

print(secondMatrix * matrix)

# To calculate an actual matrix dot product, we need to import and use the dot()

from numpy import dot
print(dot(secondMatrix, matrix))

# Matrix Stacking
from numpy import vstack, hstack

print(vstack([matrix, secondMatrix])) # add secondMatrix below matrix

print(hstack([matrix, secondMatrix])) # add secondMatrix next to matrix

# Linalg
print(matrix.shape) # a tuple of the axis lengths (3 x 3)

print(matrix.diagonal()) # array of the main diagonal entries

print(matrix.flatten()) # a flat array of all entries

print(matrix.transpose()) # mirror-image along the diagonal

print(matrix.min()) # the minimum entry

print(matrix.max()) # the maximum entry

print(matrix.mean()) # the average value of all entries

print(matrix.sum()) # the total of all entries

print(matrix.reshape(9,1)) # reshape marix

# instead of typing out our sequential list of numbers into a matrix, we could
# have imported arange() and then reshaped the sequence into a two-dimensional
# matrix:
from numpy import arange
matrix = arange(1,10) # an array of numbers 1 through 9
print(matrix)

matrix = matrix.reshape(3,3)
print(matrix)

# How about a 3d array
array3d = array([[[1,2],[3,4]], [[5,6],[7,8]], [[9,10],[11,12]]])
print(array3d)

#easier and safer way to create this particular array would be to reshape() and arange()
array3d = arange(1,13)
array3d = array3d.reshape(3,2,2)
print(array3d)

# random arrays
from numpy import random
print(random.random([3,3]))

# Some of the tools available include functionality for tasks involving optimization, integration, statistical
# tests, signal processing, Fourier transforms, image processing and more
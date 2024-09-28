import numpy as np

twoDArray = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(twoDArray)

newTwoDArray = np.insert(twoDArray, 0, [[11,22,33]], axis=1)
#   Here in insert method 1st parameter is the initial array, 2nd is the row/column no., 3rd is the row/column we need to add and last
#   is the axis. axis = 0 for row and axis = 1 for column.
print(newTwoDArray)

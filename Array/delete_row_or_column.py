import numpy as np

twoDArray = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(twoDArray)

new2dArray = np.delete(twoDArray, 1, axis = 1)
print(new2dArray)
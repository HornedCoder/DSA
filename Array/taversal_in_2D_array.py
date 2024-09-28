import numpy as np

twoDArray = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(twoDArray)

def traversal(array):
    for i in range(len(array)):  #Here length of rows can be found like this.
        for j in range(len(array[0])):
            print(array[i][j])

traversal(twoDArray)
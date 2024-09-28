import numpy as np

twoDArray = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(twoDArray)

def ls(arr,key):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if key == arr[i][j]:
                return("Key found at index " + str(i) + " " + str(j))
            
    return("No hits")
        

print(ls(twoDArray,91))
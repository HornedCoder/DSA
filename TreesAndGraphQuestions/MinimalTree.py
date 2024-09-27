'''
Ques: 
    Given a sorted (increasing order) array with unique integer elements, 
    write an algorithm to create a binary search tree with minimal height.
'''

class BSTNode():
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


def MinimalTree(sortedArray):
    if len(sortedArray) == 0:
        return None
    if len(sortedArray) == 1:
        return sortedArray[0]
    
    mid = len(sortedArray)//2
    left = MinimalTree(sortedArray[:mid])
    right = MinimalTree(sortedArray[mid+1:])
    return BSTNode(sortedArray[mid],left,right)

sortedArray = [1,2,3,4,5,6,7,8,9]
print(MinimalTree(sortedArray))
# Creating a BH Class
class BinaryHeap:
    # Main Function here.
    def __init__(self, size):
        self.customList = [None] * (size + 1)
        self.heapSize = 0
        self.maxSize = size + 1

# This Peek return the rootNode.
def peekHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.customList[1]
        
# This function returns sizeOfHeap
def sizeOfHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize

# This function does levelOrderTraversal 
def levelOrderTraversal(rootNode):
    if not rootNode:
        rootNode
    else:
        for i in range(1, rootNode.heapSize+1):
            print(rootNode.customList[i])

# The following is a helper function.
# It will check if a given index follows the Heap rule.
# Imp. Point this heapify function is for Insert. We will create one more for delete.
def heapifyTreeInsert(rootNode, index, heapType):
    parentIndex = int(index/2)
    if index <= 1:
        return
    if heapType == "Min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)
    elif heapType == "Max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)

# The following function to insert Node in Binary Heap.
def insert(rootNode, nodeValue, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "BH already full"
    rootNode.customList[rootNode.heapSize+1] = nodeValue
    rootNode.heapSize += 1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
    return "The value has been inserted"

# For extract function we need a helper function.
# This is called heapifyExtract

def heapifyTreeExtract(rootNode, index, heapType):
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChild = 0

    if rootNode.heapSize < leftIndex:
        return
    elif rootNode.heapSize == leftIndex:
        if heapType == "Min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
    else:
        if heapType == "Min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        else:
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        heapifyTreeExtract(rootNode, swapChild, heapType)

# This is the main extract node function.
# Imp point that in heap tree you can only extract the root Node.
def extractNode(rootNode, heapType):
    if rootNode.heapSize == 0:
        return
    else:
        extractedNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        heapifyTreeExtract(rootNode, 1, heapType)
        return extractedNode
    


BH = BinaryHeap(5)
insert(BH, 4, "Max")
insert(BH, 5, "Max")
insert(BH, 2, "Max")
insert(BH, 1, "Max")
levelOrderTraversal(BH)
extractNode(BH, "Max")
print("After Extract")
levelOrderTraversal(BH)
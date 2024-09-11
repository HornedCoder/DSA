import QueueUsingLL as que


#Creating a node in Binary Search Tree.
class BSTree:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

#Creating a func to insert a node in BST.
def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTree(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTree(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)

    return "The node is successfully inserted"

#Here we show preOrderTraversal
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

#inOrderTraversal
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

#postOrderTraversal
def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

#levelOrderTraversal
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQue = que.Queue()
        customQue.enqueue(rootNode)
        while not(customQue.isEmpty()):
            root = customQue.dequeue()
            print(root.value.data)
            if (root.value.leftChild) is not None:
                customQue.enqueue(root.value.leftChild)
            if (root.value.rightChild) is not None:
                customQue.enqueue(root.value.rightChild)

#Searching a node.
def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        return print("Value",nodeValue,"found")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild == None:
            return print("Value",nodeValue,"not found") 
        elif rootNode.leftChild.data == nodeValue:
            return print("Value",nodeValue,"found")                    
        else:
            searchNode(rootNode.leftChild, nodeValue)
    else :
        if rootNode.rightChild == None:
            return print("Value",nodeValue,"not found")  
        elif rootNode.rightChild.data == nodeValue:
            return print("Value",nodeValue,"found")
        else:
            searchNode(rootNode.rightChild, nodeValue)

# Creating a helper function for deleting a node.
# This function will give the Node with min value so that it can be
# used as a replacement for deleting a node with two children.

def minValueNode(bstNode):
    current = bstNode
    while (current.leftChild) is not None:
        current = current.leftChild
    return current

def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild,nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild,nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        
        temp = minValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild,temp.data)
    return rootNode
#Here we excute all the functions by initiating values. Main function.
newBST = BSTree(None)
print(insertNode(newBST,7))
print(insertNode(newBST,8))
print(insertNode(newBST,4))
print(insertNode(newBST,6))
print(insertNode(newBST,10))
#print(newBST.data)
#print(newBST.rightChild.data)
print("PreOrder:")
preOrderTraversal(newBST)
print("InOrder:")
inOrderTraversal(newBST)
print("PostOrder:")
postOrderTraversal(newBST)
print("levelOrderTraversal")
levelOrderTraversal(newBST)
searchNode(newBST, 13)
deleteNode(newBST, 7)
print("After deletion")
levelOrderTraversal(newBST)


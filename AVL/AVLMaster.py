import QueueUsingLL as que


#Creating a node in AVL Tree.
class AVLTree:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1


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

#The following function will be used as helper function.
# Getting Height of Node
def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height

#The two functions below helps in balancing the AVL tree by rotation method.
def rightRotate(disbalanceNode):
    newRoot = disbalanceNode.leftChild
    disbalanceNode.leftChild = disbalanceNode.leftChild.rightChild
    newRoot.rightChild = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.rightChild), getHeight(disbalanceNode.leftChild))
    newRoot.height = 1 + max(getHeight(newRoot.rightChild), getHeight(newRoot.leftChild))
    return newRoot

def leftRotate(disbalanceNode):
    newRoot = disbalanceNode.rightChild
    disbalanceNode.rightChild = disbalanceNode.rightChild.leftChild
    newRoot.leftChild = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.rightChild), getHeight(disbalanceNode.leftChild))
    newRoot.height = 1 + max(getHeight(newRoot.rightChild), getHeight(newRoot.leftChild))
    return newRoot

#This funnction checks the balance on nodes.
def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

#This is the Insert Node function.
def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVLTree(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)
    
    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    if balance > 1 and nodeValue < rootNode.leftChild.data:
        return rightRotate(rootNode)
    if balance > 1 and nodeValue > rootNode.leftChild.data:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)

    if balance < -1 and nodeValue > rootNode.rightChild.data:
        return leftRotate(rootNode)
    if balance < -1 and nodeValue < rootNode.rightChild.data:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    
    return rootNode

#The following is a helper function to delete node.
#This function gets the min Value node.

def getMinValueNode(rootNode):
    if rootNode is None or rootNode.leftChild is None:
        return rootNode
    return getMinValueNode(rootNode.leftChild)

#Now the main delete method
def deleteNode(rootNode, nodeValue):
    if not rootNode:
        return rootNode
    elif nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        elif rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        temp = getMinValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) >= 0:
        return rightRotate(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) <= 0:
        return leftRotate(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) > 0:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) < 0:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    
    return rootNode

    


newAVL = AVLTree(5)
newAVL = insertNode(newAVL, 10)
newAVL = insertNode(newAVL, 15)
newAVL = insertNode(newAVL, 20)
print("LOT")
levelOrderTraversal(newAVL)
newAVL = deleteNode(newAVL, 15)
print("After delete:")
levelOrderTraversal(newAVL)

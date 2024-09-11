import QueueUsingLL as que

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
    
BTRootNode = TreeNode('Drinks')
LChild = TreeNode('Hot')
RChild = TreeNode('Cold')
BTRootNode.leftChild = LChild
BTRootNode.rightChild = RChild

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

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

def search(rootNode, key):
    if not rootNode:
        return "Not Found"
    else:
        customQue = que.Queue()
        customQue.enqueue(rootNode)
        while not(customQue.isEmpty()):
            root = customQue.dequeue()
            if (root.value.data == key):
                return "Found"
            if (root.value.leftChild is not None):
                customQue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQue.enqueue(root.value.rightChild)
        return "Not Found"            
    
def insert(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
        return "Successfully Inserted"
    else:
        customQue = que.Queue()
        customQue.enqueue(rootNode)
        while not (customQue.isEmpty()):
            root = customQue.dequeue()
            if root.value.leftChild is not None:
                customQue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "Successfully Inserted"
            if root.value.rightChild is not None:
                customQue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "Successfully Inserted"
        
def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQue = que.Queue()
        customQue.enqueue(rootNode)
        while not (customQue.isEmpty()):
            root = customQue.dequeue()
            if (root.value.leftChild) is not None:
                customQue.enqueue(root.value.leftChild)
            if (root.value.rightChild) is not None:
                customQue.enqueue(root.value.rightChild)

        return root.value

def deleteDeepestNode(rootNode,DNode):
    if not rootNode:
        return
    else:
        customQue = que.Queue()
        customQue.enqueue(rootNode)
        while not(customQue.isEmpty()):
            root = customQue.dequeue()
            if root.value is DNode:
                root.value = None
                return
            if root.value.rightChild:
                if root.value.rightChild is DNode:
                    root.value.rightChild = None
                    return
                else:
                    customQue.enqueue(root.value.rightChild)
            if root.value.leftChild:
                if root.value.leftChild is DNode:
                    root.value.leftChild = None
                    return
                else:
                    customQue.enqueue(root.value.leftChild)        

def deleteNode(rootNode, GNode):
    if not rootNode:
        return "No Tree Present."
    else:
        customQue = que.Queue()
        customQue.enqueue(rootNode)
        while not (customQue.isEmpty()):
            root = customQue.dequeue()
            if root.value.data == GNode:
                DNode = getDeepestNode(rootNode)
                root.value.data = DNode.data
                deleteDeepestNode(rootNode, DNode)
                return "The node has been successfully deleted"
            if (root.value.leftChild) is not None:
                customQue.enqueue(root.value.leftChild)
            if (root.value.rightChild) is not None:
                customQue.enqueue(root.value.rightChild)
        return "Failed to delete."
            




print("The following is the preOrderTraversal:")
preOrderTraversal(BTRootNode)
print("The following is the inOrderTraversal:")
inOrderTraversal(BTRootNode)
print("The following is the postOrderTraversal:")
postOrderTraversal(BTRootNode)
print("The following is the levelOrderTraversal:")
levelOrderTraversal(BTRootNode)
print(search(BTRootNode, "Hot"))
newNode = TreeNode("Tea")
insert(BTRootNode, newNode)
newNode2 = TreeNode("Coffee")
insert(BTRootNode, newNode2)
newNode3 = TreeNode("Cola")
insert(BTRootNode, newNode3)
levelOrderTraversal(BTRootNode)
ans = getDeepestNode(BTRootNode)
print("Deepest node is:",ans.data)
'''deleteDeepestNode(BTRootNode, ans)
print("New Tree after deleting deepestNode")
levelOrderTraversal(BTRootNode)
'''
print(deleteNode(BTRootNode, "Tea"))
print("New Tree after deleting deepestNode")
levelOrderTraversal(BTRootNode)
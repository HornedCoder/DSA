#Here we are creating a BT Using List.
class BinaryTree:
    def __init__(self, size):
        self.customList = size*[None]
        self.lastUsedIndex = 0
        self.maxSize = size
    
    #Here we will write a func to insert Node in Tree.
    def insert(self, value):
        if self.lastUsedIndex+1 == self.maxSize:
            return "Tree is already full."
        self.customList[self.lastUsedIndex+1] = value
        self.lastUsedIndex += 1
        return "Value added successfully."
    
    #Here we will create a func to search a Node.
    def search(self, key):
        for i in self.customList:
            if i == key:
                return "Found"
        return "Not Found"
    
    #Here we will create a code for preOrderTraversal.
    def preOrderTraversal(self, index=1):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2 + 1)

    #Here we will try inOrderTraversal.
    def inOrderTraversal(self, index=1):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index*2)
        print(self.customList[index])
        self.inOrderTraversal(index*2 +1)

    #Here we will try postOrderTraversal.
    def postOrderTraversal(self, index=1):
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(index*2)
        self.postOrderTraversal(index*2 +1)
        print(self.customList[index])

    #Here we will try levelOrderTraversal
    def levelOrderTraversal(self):
        for i in range(1, self.lastUsedIndex+1):
            print(self.customList[i])

    #Here we will delete a node.
    def deleteNode(self, nodeV):
        if self.lastUsedIndex == 0:
            return "No node to delete"
        for i in range(1, self.lastUsedIndex+1):
            if self.customList[i] == nodeV:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "The node has been successfully deleted."

newBT = BinaryTree(8)
print(newBT.insert("Drinks"))
print(newBT.insert("Hot"))
print(newBT.insert("Cold"))
print(newBT.insert("Tea"))
print(newBT.insert("Coffee"))
#When we print the List we can see index 0 is None.
#That is because of mathmatical simplicity.
print(newBT.customList)
print(newBT.search("Hot"))
print("The following is the preOrderTraversal of the BT.")
newBT.preOrderTraversal()
print("The following is the inOrderTraversal of the BT.")
newBT.inOrderTraversal()
print("The following is the postOrderTraversal of the BT.")
newBT.postOrderTraversal()
print("The following is the levelOrderTraversal of the BT.")
newBT.levelOrderTraversal()
newBT.deleteNode("Hot")
print(newBT.customList)
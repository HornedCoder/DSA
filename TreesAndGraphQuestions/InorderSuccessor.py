'''
Ques:   Write an algorithm to find the next node (i.e in-order successor)
        of given node in a binary search tree. You may assume that each node 
        has a link to its parent.
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(node,data):
    if node is None:
        return Node(data)
    
    else:
        if data <= node.data:
            temp = insert(node.left,data)
            node.left = temp
            temp.parent = node
        else:
            temp = insert(node.right,data)
            node.right = temp
            temp.parent = node
        return node

#   Helper function to find the min in the rigght subtree.
def findMin(node):
    current = node
    while current.left:
        current = current.left
    return current

def inOrderSuccessor(node):
    if not Node:
        return None

    if node.right is not None:
        temp = findMin(node.right)
        return temp

    current = node
    parent = current.parent
    while parent and current == parent.right:
        current = parent
        parent = parent.parent

    return parent

root = None
root = insert(root,4)
root = insert(root,2)
root = insert(root,8)
root = insert(root,1)
root = insert(root,3)
root = insert(root,5)
root = insert(root,9)

temp = root.left
successor = inOrderSuccessor(temp)

if successor is None:
    print('None')
else:
    print(successor.data)





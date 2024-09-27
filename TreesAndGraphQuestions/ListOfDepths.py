'''
Ques:
    Given a binary search tree, design an algorithm which creates 
    a linked list of all the nodes at each depth 
    (ie , if you have a tree with depth D, you will have D linked lists)
'''

from turtle import right


class LinkedList():
    def __init__(self, val):
        self.val = val
        self.next = None

    def add(self, val):
        if self.next == None:
            self.next = LinkedList(val)
        else:
            self.next.add(val)

    def __str__(self):
        return "({val})".format(val = self.val) + str(self.next)
    
class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def depth(tree):
    if tree == None:
        return 0
    if tree.left == None and tree.right == None:
        return 1
    else:
        leftDepth = 1+depth(tree.left)
        rightDepth = 1+depth(tree.right)

        if leftDepth > rightDepth:
            return leftDepth
        else:
            return rightDepth
    
def treeToLinkedList(tree, customDict = {}, d = None):
    if d == None:
        d = depth(tree)
    
    if customDict.get(d) == None:
        customDict[d] = LinkedList(tree.val)
    else:
        customDict[d].add(tree.val)
        if d == 1:
            return customDict
    
    if tree.left != None:
        treeToLinkedList(tree.left,customDict,d-1)
    if tree.right != None:
        treeToLinkedList(tree.right,customDict,d-1)

    return customDict


mainTree = BinaryTree(1)
two = BinaryTree(2)
three = BinaryTree(3)
four = BinaryTree(4)
five = BinaryTree(5)
six = BinaryTree(6)
seven = BinaryTree(7)
mainTree.left = two
mainTree.right = three
two.left = four
two.right = five
three.left = six
three.right = seven

customDict  = treeToLinkedList(mainTree)

for depthLevel, linkedList in customDict.items():
    print("{0} {1}".format(depthLevel, linkedList))

    
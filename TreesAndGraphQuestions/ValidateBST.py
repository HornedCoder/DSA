'''
Ques:
    Implement a function to check if a binary tree is a Binary Search Tree.
'''


class TreeNode:
     def __init__(self, value):
         self.val = value
         self.left = None
         self.right = None


def isValidBST(root):
    # TODO
    if root == None:
        return True
        
    if root.left == None and root.right == None:
        return True
        
    if root.val < root.left.val:
        return False
    else:
        isValidBST(root.left)
    
    if root.val > root.right.val:
        return False
    else:
        isValidBST(root.right)
        
    return True


rootTree = TreeNode(4)
one = TreeNode(1)
three = TreeNode(3)
two = TreeNode(2)
five = TreeNode(5)

rootTree.left = one
rootTree.right = three
three.left = two
three.right = five

print(isValidBST(rootTree))



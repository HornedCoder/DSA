class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def check_balance(root):

    def check_balance_and_height(node):
        # Base case: an empty tree is balanced and has height -1
        if not node:
            return True, -1
        
        # Traverse the left and right subtrees
        left_balance, left_height = check_balance_and_height(node.left)
        if not left_balance:
            return False, 0
        right_balance, right_height = check_balance_and_height(node.right)
        if not right_balance:
            return False, 0
        
        # If the tree is balanced, return True and the height of the tree
        if abs(left_height - right_height) > 1:
            return False, 0
        else:
            return True, max(left_height, right_height) + 1
    
    return check_balance_and_height(root)

# Example usage:
# Constructing a simple binary tree:
#        1
#       / \
#      2   3
#     / \
#    4   5
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(check_balance(root))  # Output: True  

# Constructing an unbalanced binary tree:
#        1
#       / \
#      2   3
#     / \
#    4   5
#   /
#  6
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)

print(check_balance(root))  # Output: False 

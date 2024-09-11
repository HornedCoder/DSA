class TreeNode:
    def __init__(self,data,children=[]):
        self.data = data
        self.children = children
    
    def __str__(self, level = 0):
        res = " " * level + str(self.data) + "\n"
        for child in self.children:
            res += child.__str__(level+1)
        return res
    
    def addChild(self,TreeNode):
        self.children.append(TreeNode)

newTree = TreeNode("Drinks",[])
hot = TreeNode('Hot',[])
cold = TreeNode('Cold',[])
tea = TreeNode('Tea',[])
coffee = TreeNode('Coffee',[])
cola = TreeNode('Cola',[])
fantaLight = TreeNode('Fanta Light Bruv',[])
newTree.addChild(hot)
newTree.addChild(cold)
hot.addChild(tea)
hot.addChild(coffee)
cold.addChild(cola)
cold.addChild(fantaLight)
print(newTree)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()

#   Here we go with the Insert function.
    def insertString(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch:node})
            current = node
        current.endOfString = True
        print("Successfully Inserted")

#   Search function.
    def search(self, word):
        current = self.root
        for i in word:
            node = current.children.get(i)
            if node == None:
                return False
            current = node
        
        if current.endOfString == True:
            return True
        else:
            return False

            

newTrie = Trie()
newTrie.insertString("App")
newTrie.insertString("Appl")
print(newTrie.search("App"))
print(newTrie.search("Ap"))

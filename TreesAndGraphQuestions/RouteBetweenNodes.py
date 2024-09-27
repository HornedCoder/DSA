'''
Ques:
Given a directed graph and two nodes (S and E),
design an algorithm to find out whether there is a route from S to E.
'''


class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)
    
    def checkRoute(self, startNode, endNode):
        queue = []
        queue.append([startNode])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == endNode:
                return True
            for adjacent in self.gdict[node]:
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
        return False


customDict = { "a" : ["c","d","b"],
            "b" : ["j"],
            "c" : ["g"],
            "d" : [],
            "e" : ["f", "a"],
            "f" : ["i"],
            "g" : ["d", "h"],
            "h" : [],
            "i" : [],
            "j" : []
               }
 
g = Graph(customDict)
print(g.checkRoute("a", "j")) #True
from collections import defaultdict

class Graph:
    def __init__(self, noOfVertices):
        self.graph = defaultdict(list)
        self.noOfVertices = noOfVertices
    
    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def topologicalHelper(self, v, visited, stack):
        visited.append(v)

        for i in self.graph[v]:
            if i not in visited:
                self.topologicalHelper(i, visited, stack)

        stack.insert(0, v)

    def topologicalSort(self):
        visited = []
        stack = []

        for k in list(self.graph):
            if k not in visited:
                self.topologicalHelper(k, visited, stack)
        
        print(stack)

custGraph = Graph(8)
custGraph.addEdge('A','C')
custGraph.addEdge('C','E')
custGraph.addEdge('E','H')
custGraph.addEdge('E','F')
custGraph.addEdge('F','G')
custGraph.addEdge('B','D')
custGraph.addEdge('B','C')
custGraph.addEdge('D','F')

custGraph.topologicalSort()
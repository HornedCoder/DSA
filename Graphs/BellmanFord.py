class Graph:

    def __init__(self, vertices):
        self.v = vertices
        self.graph = []
        self.nodes = []

    def add_edge(self,s,d,w):
        self.graph.append([s,d,w])

    def add_node(self,value):
        self.nodes.append(value)

    def print_Sol(self,dist):
        print("Vertex Distance from source")
        for key, value in dist.items():
            print(' '+ key, ': ',value)

    def bellman_ford(self, src):

        dist = {i : float('inf') for i in self.nodes}
        dist[src] = 0

        for _ in range(self.v-1):
            for s,d,w in self.graph:
                if dist[s] != float('inf') and dist[s] + w < dist[d]:
                    dist[d] = dist[s]+w
            
            for s,d,w in self.graph:
                if dist[s] != float('inf') and dist[s] + w < dist[d]:
                    print("Graph has -ve rizz")
            

        self.print_Sol(dist)


g = Graph(5)
g.add_node("A")
g.add_node("B")
g.add_node("C")
g.add_node("D")
g.add_node("E")
g.add_edge("A","C",6)
g.add_edge("A","D",6)
g.add_edge("B","A",3)
g.add_edge("C","D",1)
g.add_edge("D","C",2)
g.add_edge("D","B",1)
g.add_edge("E","B",4)
g.add_edge("E","D",2)
g.bellman_ford("E")




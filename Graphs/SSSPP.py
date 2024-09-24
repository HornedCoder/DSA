class Graph:

    def  __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def bfs(self, start, end):
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for adjacent in self.gdict[node]:
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
                
cdist = {
    'A':['B','C'],
    'B':['D','G'],
    'C':['D','E'],
    'D':['F'],
    'E':['F'],
    'G':['F']
}

g = Graph(cdist)
print(g.bfs('A','F'))
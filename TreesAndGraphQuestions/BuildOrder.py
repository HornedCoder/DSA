#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# Build Order

# projects a,b,c,d,e,f
# dependencies: (a,d), (f,b), (b,d), (f,a), (d,c)

def createGraph(projects, dependencies):
    projectGraph = {}
    for project in projects:
        projectGraph[project] = []
    for pairs in dependencies:
        projectGraph[pairs[0]].extend(pairs[1])
    return projectGraph

project = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a','d'), ('f','b'), ('b','d'), ('f','a'), ('d','c')]

graph = createGraph(project, dependencies)

print(graph)

def getProjectWithDependencies(graph):
    projectWithDependencies = set()
    for project in graph:
        projectWithDependencies = projectWithDependencies.union(set(graph[project]))
    return projectWithDependencies
    
ProjectWD = getProjectWithDependencies(graph)    
print(ProjectWD)

def getProjectWithoutDependencies(graph, projectWD):
    projectWithotDependencies = set()
    for project in graph:
        if project not in projectWD:
            projectWithotDependencies.add(project)
    return projectWithotDependencies

print(getProjectWithoutDependencies(graph, getProjectWithDependencies(graph)))


def findBuilder(project, dependencies):
    buildOrder = []
    graph = createGraph(project, dependencies)
    while graph:
        projectWithDependencies = getProjectWithDependencies(graph)
        projectWithoutDependencies = getProjectWithoutDependencies(graph, getProjectWithDependencies(graph))
        if len(projectWithoutDependencies) == 0 and graph:
            raise ValueError("There is a cycle")
        for independentProject in projectWithoutDependencies:
            buildOrder.append(independentProject)
            del graph[independentProject]
    return buildOrder
    
    
print(findBuilder(project, dependencies))
    
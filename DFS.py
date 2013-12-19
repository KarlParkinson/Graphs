from Graph import Graph
from Vertex import Vertex
import random


def DFS(graph, start):
    start.setVisited(True)
    for neighbour in start.getNeighbours():
        if (not neighbour.getVisited()):
            print(str(start.getId()) + "->" + str(neighbour.getId()))
            DFS(graph, neighbour)

g = Graph()
for i in range(0, 14):
    g.addVertex(i)

g.addEdge(0, 1, 0)
g.addEdge(0, 2, 0)
g.addEdge(0, 9, 0)
g.addEdge(1, 3, 0)
g.addEdge(1, 8, 0)
g.addEdge(3, 6, 0)
g.addEdge(2, 17, 0)
g.addEdge(9, 7, 0)
g.addEdge(9, 12, 0)
#for i in range(0, 20):
 #   for j in range(0, 20):
  #      g.addEdge(i, j, 0)
        
DFS(g, g.vertices[0])
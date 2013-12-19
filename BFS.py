from Graph import Graph
from Vertex import Vertex
import random



def BFS(graph, start):
    for v in g:
        v.setVisited(False)
    start.setVisited(True)
    q = []
    q.append(start)
    while(len(q) != 0):
        current = q.pop()
        for neighbour in current.getNeighbours():
            if(not neighbour.getVisited()):
                neighbour.setVisited(True)
                print(str(start.getId()) + "->" + str(neighbour.getId()))
                #print(str(neighbour.getId()))
                q.append(neighbour)
            
            


g = Graph()
for i in range(0, 20):
    g.addVertex(i)
    
for i in range(0, 20):
    for j in range(i+1, 20):
        g.addEdge(i, j, 0)
        
BFS(g, g.vertices[11])
        

                  
        
    
    
from Graph import Graph
from Vertex import Vertex
from MST import findMin, findNode

class PathfindingNode:
    def __init__(self, vertex):
            self.vertex = vertex
            self.distance = None
            self.parent = None
            
    def getVertex(self):
        return self.vertex
        
    def getDistance(self):
        return self.distance
        
    def setDistance(self, distance):
        self.distance = distance
            
    def getParent(self):
        return self.parent
        
    def setParent(self, newParent):
        self.parent = newParent    


# 0 -> unseen
# 1 -> fringe
# 2 -> inTree
def dijkstrasAlgorithm(graph, start):
    for v in graph:
        v.setStatus(0)
        
    start.setStatus(2)
    pathTree = []
    fringeList = []
    current = start
    current.setDistance(0)
    pathTree.append(current)
    while (len(minTree) < graph.order):
        #minTree.append(current)
        for neighbour in current.getNeighbours():
            if (neighbour.getStatus() == 0):
                node = PathfindingNode(neighbour)
                neighbour.setStatus(1)
                node.setParent(current)
                node.setDistance(current.getDistance() + neighbours[neighbour])
                fringeList.insert(0, node)
                #neighbour.setParent(current)
                # add weight of edge to priority queue
            elif (neighbour.getStatus() == 1):
                node = findNode(fringeList, neighbour)
                if (node.Distance() > (current.getDistance() + neighbours[neighbour])):
                    node.setDistance(current.getDistance() + neighbours[neighbour])
                    node.setParent(current)
        minWeight = findMin(fringeList)
        print(str(minWeight.getParent().getId()) + "->" + str(minWeight.getVertex().getId()))
        current = minWeight.getVertex()
        fringeList.remove(minWeight)
        current.setStatus(2)
        pathTree.append(current)
    
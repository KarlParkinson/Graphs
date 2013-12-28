from Graph import Graph
from Vertex import Vertex
from MST import findMin, findNode
from PriorityQueue import PriorityQueue

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
        
# 0 -> unseen
# 1 -> fringe
# 2 -> inTree
def dijkstrasAlgorithm(graph, start):
    for v in graph:
        v.setStatus(0)
        
    #start.setStatus(2)
    start.setDistance(0)
    pq = PriorityQueue()
    #heapq.heappush(pq, (0, start))
    pq.enQueue((0, start))
    while (not pq.isEmpty()):
        current = pq.deQueue()[1]
        current.setStatus(2)
        #if(current.getParent() != None):
            #  print(str(current.getParent().getId()) + "->" + str(current.getId()))
        for neighbour in current.getNeighbours():
            if (neighbour.getStatus() == 0):        
                neighbour.setStatus(1)
                neighbour.setParent(current)
                neighbour.setpqWeight(current.neighbours[neighbour])
                neighbour.setDistance(current.getDistance() + current.neighbours[neighbour])
                pq.enQueue((neighbour.getpqWeight(), neighbour))
            elif (neighbour.getStatus() == 1):
                if (neighbour.getDistance()) > (current.getDistance() + current.neighbours[neighbour]):
                    #old = (neighbour.getpqWeight(), neighbour)
                    #neighbour.setpqWeight(current.neighbours[neighbour])
                    #pq.updatePriority(old, (neighbour.getpqWeight(), neighbour))
                    neighbour.setParent(current)
                    neighbour.setDistance(current.getDistance() + current.neighbours[neighbour])
    
    
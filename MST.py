from Graph import Graph
from Vertex import Vertex
from PriorityQueue import PriorityQueue


class Node:
    def __init__(self, vertex):
        self.vertex = vertex
        self.weight = None
        self.parent = None
        
    def getVertex(self):
        return self.vertex
    
    def getWeight(self):
        return self.weight
    
    def setWeight(self, weight):
        self.weight = weight
        
    def getParent(self):
        return self.parent
    
    def setParent(self, newParent):
        self.parent = newParent
        
    


    
# 0 -> unseen
# 1 -> fringe
# 2 -> inTree
def primsAlgorithm(graph, start):
    for v in graph:
        v.setStatus(0)
        
    start.setStatus(2)
    minTree = []
    fringeList = []
    current = start
    minTree.append(current)
    while (len(minTree) < graph.order):
        #minTree.append(current)
        for neighbour in current.getNeighbours():
            if (neighbour.getStatus() == 0):
                node = MSTNode(neighbour)
                neighbour.setStatus(1)
                node.setParent(current)
                node.setWeight(current.neighbours[neighbour])
                fringeList.insert(0, node)
                #neighbour.setParent(current)
                # add weight of edge to priority queue
            elif (neighbour.getStatus() == 1):
                node = findNode(fringeList, neighbour)
                if (node.getWeight() > current.neighbours[neighbour]):
                    node.setWeight(current.neighbours[neighbour])
                    node.setParent(current)
        minWeight = findMin(fringeList)
        print(str(minWeight.getParent().getId()) + "->" + str(minWeight.getVertex().getId()))
        current = minWeight.getVertex()
        fringeList.remove(minWeight)
        current.setStatus(2)
        minTree.append(current)
    
    return fringeList

# 0 -> unseen
# 1 -> fringe
# 2 -> inTree
def primsAlgorithm2(graph, start):
    for v in graph:
        v.setStatus(0)
        
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
                        pq.enQueue((neighbour.getpqWeight(), neighbour))
                    elif (neighbour.getStatus() == 1):
                        if (neighbour.getpqWeight() > current.neighbours[neighbour]):
                            old = (neighbour.getpqWeight(), neighbour)
                            neighbour.setpqWeight(current.neighbours[neighbour])
                            pq.updatePriority(old, (neighbour.getpqWeight(), neighbour))
                            neighbour.setParent(current)
    
                            

def findMin(nodeList):
    minimum = nodeList[0].getWeight()
    minNode = nodeList[0]
    for node in nodeList:
        if (node.getWeight() < minimum):
            minNode = node
    return minNode

def findNode(nodeList, vertex):
    for node in nodeList:
        if (node.getVertex() == vertex):
            return node
             
             


g = Graph()
a = g.addVertex("a")
b = g.addVertex("b")
c = g.addVertex("c")
#d = g.addVertex("d")

g.addEdge(a, b, 7)
g.addEdge(a, c, 2)
g.addEdge(b, c, 5)
#g.addEdge(d, a, 1)
#g.addEdge(a, c, 0)

primsAlgorithm2(g, a)

        
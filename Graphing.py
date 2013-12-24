import pygame
import random
import sys
import time

from pygame.locals import *

from Graph import Graph, DrawableGraph
from Vertex import Vertex, DrawableVertex
from MST import Node
from Pathfinding import PathfindingNode

def drawEdges(graph, surface):
    startFound = False
    startVertex = None
    endVertex = None
    while True:
        #print("hello")
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                for v in graph:
                    if(v.clickedOn(event.pos) and not startFound):
                        startFound = True
                        startVertex = v
                    elif(v.clickedOn(event.pos) and startFound):
                        endVertex = v
                        graph.addEdge(startVertex, endVertex, random.randint(0, 10))
                        graph.drawGraph(surface)
                        pygame.display.update()
                        startFound = False
            if event.type == KEYDOWN:
                return
            
def handleBFS(graph, surface):
    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                for v in graph:
                    if(v.clickedOn(event.pos)):
                        BFS(graph, v, surface)
                        return    
            
def handleDFS(graph, surface):
    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                for v in graph:
                    if(v.clickedOn(event.pos)):
                        startVertex = v
                        for v in graph:
                            v.setVisited(False, "black")
                            #v.draw(surface)
                        DFS(graph, startVertex, surface)
                        return
                

def newVertex(graph, pos):
    graph.addDrawableVertex(pos, random.randint(0, 800))
    
def BFS(graph, start, surface):
    for v in g:
        v.setVisited(False, "black")
    start.setVisited(True, "red")
    q = []
    q.append(start)
    start.draw(surface)
    pygame.display.update()
    time.sleep(0.5)
    while(len(q) != 0):
        current = q.pop()
        #current.draw(surface)
        #pygame.display.update()
        #time.sleep(0.5)
        for neighbour in current.getNeighbours():
            if(not neighbour.getVisited()):
                neighbour.setVisited(True, "red")
                neighbour.draw(surface)
                pygame.display.update()
                time.sleep(0.5)
                #print(str(current.getId()) + "->" + str(neighbour.getId()))
                #print(str(neighbour.getId()))
                q.append(neighbour)
                
def DFS(graph, start, surface):
    start.setVisited(True, "green")
    start.draw(surface)
    pygame.display.update()
    time.sleep(0.5)
    for neighbour in start.getNeighbours():
        if (not neighbour.getVisited()):
            #print(str(start.getId()) + "->" + str(neighbour.getId()))
            DFS(graph, neighbour, surface)
            
def handlePrims(graph, surface):
    while True:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    for v in graph:
                        if(v.clickedOn(event.pos)):
                            startVertex = v                     
                            primsAlgorithm(graph, startVertex, surface)
                            return    
            
def primsAlgorithm(graph, start, surface):
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
                node = Node(neighbour)
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
        graph.drawEdge(minWeight.getParent(), minWeight.getVertex(), surface, "yellow")
        time.sleep(0.5)
        #print(str(minWeight.getParent().getId()) + "->" + str(minWeight.getVertex().getId()))
        current = minWeight.getVertex()
        fringeList.remove(minWeight)
        current.setStatus(2)
        minTree.append(current)
    
    #return fringeList
    
def handleDijkstra(graph, surface):
    while True:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    for v in graph:
                        if(v.clickedOn(event.pos)):
                            startVertex = v                     
                            dijkstrasAlgorithm(graph, startVertex, surface)
                            return  
    
# 0 -> unseen
# 1 -> fringe
# 2 -> inTree
def dijkstrasAlgorithm(graph, start, surface):
    for v in graph:
        v.setStatus(0)
        
    start.setStatus(2)
    pathTree = []
    fringeList = []
    current = start
    current.setDistance(0)
    pathTree.append(current)
    while (len(pathTree) < graph.order):
        #minTree.append(current)
        for neighbour in current.getNeighbours():
            if (neighbour.getStatus() == 0):
                node = Node(neighbour)
                neighbour.setStatus(1)
                node.setParent(current)
                neighbour.setDistance(current.getDistance() + current.neighbours[neighbour])
                node.setWeight(current.neighbours[neighbour])
                fringeList.insert(0, node)
                #neighbour.setParent(current)
                # add weight of edge to priority queue
            elif (neighbour.getStatus() == 1):
                node = findNode(fringeList, neighbour)
                if (neighbour.getDistance() > (current.getDistance() + current.neighbours[neighbour])):
                    neighbour.setDistance(current.getDistance() + current.neighbours[neighbour])
                    node.setParent(current)
        minWeight = findMin(fringeList)
        #print(str(minWeight.getParent().getId()) + "->" + str(minWeight.getVertex().getId()))
        graph.drawEdge(minWeight.getParent(), minWeight.getVertex(), surface, "blue")
        time.sleep(0.5)
        current = minWeight.getVertex()
        fringeList.remove(minWeight)
        current.setStatus(2)
        pathTree.append(current)


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
            


g = DrawableGraph()
#a = g.addDrawableVertex((240, 75), 1)
#b = g.addDrawableVertex((175, 150), 2)
#c = g.addDrawableVertex((305, 150), 3)
#d = g.addDrawableVertex((145, 225), 4)
#e = g.addDrawableVertex((205, 225), 5)
#f = g.addDrawableVertex((275, 225), 6)
#h = g.addDrawableVertex((335, 225), 7)

#g.addEdge(a, b)
#g.addEdge(a, c)
#g.addEdge(b, d)
#g.addEdge(b, e)
#g.addEdge(c, f)
#g.addEdge(c, h)
#g.addEdge(a, h)


pygame.init()
width = 800
height = 800

window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
window.fill(pygame.Color("white"))
pygame.display.update()

g.drawGraph(window)
pygame.display.update()
#BFS(g, a)

#for i in range(0, 5):
 #   g.addVertex(i)
    
#for i in range(0, 5):
 #   for j in range(0, 5):
  #      g.addEdge(i, j, 0)


#g.printGraph()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == MOUSEBUTTONDOWN:
            #BFS(g, a, window)
            #DFS(g, a, window)
            newVertex(g, event.pos)
            g.drawGraph(window)
            pygame.display.update()

            
        if event.type == KEYDOWN:
            #print(event.key)
            if event.key == 304:
                #print("shift")
                drawEdges(g, window)
            if event.key == 100:
                handleDFS(g, window)
            if event.key == 98:
                handleBFS(g, window)
            if event.key == 112:
                handlePrims(g, window)
            if event.key == 115:
                handleDijkstra(g, window)
                
        
        #g.drawGraph(window)
        #pygame.display.update()                       
            #for v in g:
                #v.setVisited(False, "black")
            #DFS(g, a, window)
            

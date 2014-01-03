import time

from tkinter import *
from Graph import Graph, DrawableGraph
from Vertex import Vertex, DrawableVertex
from PriorityQueue import PriorityQueue

class AlgorithmHandler:
    
    def __init__(self, canvas):
        self.canvas = canvas
        
        
    def DFS(self, graph, start, canvas):
        start.setVisited(True)
        start.setColour("green")
        start.draw(canvas)
        canvas.update()
        time.sleep(0.5)
        for neighbour in start.getNeighbours():
            if (not neighbour.getVisited()):
                #print(str(start.getId()) + "->" + str(neighbour.getId()))
                self.DFS(graph, neighbour, canvas)  
                
    def BFS(self, graph, start, surface):
        for v in graph:
            v.setVisited(False)
        start.setVisited(True)
        start.setColour("red")
        q = []
        q.append(start)
        start.draw(surface)
        surface.update()
        time.sleep(0.5)
        while(len(q) != 0):
            current = q.pop()
            for neighbour in current.getNeighbours():
                if(not neighbour.getVisited()):
                    neighbour.setVisited(True)
                    neighbour.setColour("red")
                    neighbour.draw(surface)
                    surface.update()
                    time.sleep(0.5)
                    q.append(neighbour)  
                    
    def prims(self, graph, start, canvas):
        for v in graph:
            v.setStatus(0)
            v.setParent(None)
                
        pq = PriorityQueue()
        #heapq.heappush(pq, (0, start))
        pq.enQueue((0, start))
        while (not pq.isEmpty()):
            current = pq.deQueue()[1]
            current.setStatus(2)
            if(current.getParent() != None):
                graph.drawEdge(current.getParent(), current, canvas, "yellow")
                canvas.update()
                time.sleep(0.5)
                #print(str(current.getParent().getId()) + "->" + str(current.getId()))
            for neighbour in current.getNeighbours():
                if (neighbour.getStatus() == 0):        
                    neighbour.setStatus(1)
                    neighbour.setParent(current)
                    neighbour.setpqWeight(current.neighbours[neighbour])
                    #print(str(neighbour.getpqWeight()))
                    pq.enQueue((neighbour.getpqWeight(), neighbour))
                elif (neighbour.getStatus() == 1):
                    if (neighbour.getpqWeight() > current.neighbours[neighbour]):
                        old = (neighbour.getpqWeight(), neighbour)
                        neighbour.setpqWeight(current.neighbours[neighbour])
                        pq.updatePriority(old, (neighbour.getpqWeight(), neighbour))
                        neighbour.setParent(current)
                        
    def dijkstras(self, graph, start, canvas):
        pq = PriorityQueue()
        for v in graph:
            v.setStatus(0)
            v.setDistance(float("inf"))
            #print((v.getDistance(), v))
            pq.enQueue((v.getDistance(), v))
                    
        #start.setStatus(2)
        start.setDistance(0)
        pq.updatePriority((float("inf"), start), (0, start))
        #heapq.heappush(pq, (0, start))
        #pq.enQueue((0, start))
        #while (not pq.isEmpty()):
        for i in range(0, graph.order):
            current = pq.deQueue()[1]
            current.setStatus(2)
            if(current.getParent() != None):
                graph.drawEdge(current.getParent(), current, canvas, "blue")
                canvas.update()
                time.sleep(0.5)            
            for neighbour in current.getNeighbours():
                if (neighbour.getDistance()) > (current.getDistance() + current.neighbours[neighbour]):
                    old = (neighbour.getDistance(), neighbour)
                    neighbour.setParent(current)
                    neighbour.setDistance(current.getDistance() + current.neighbours[neighbour]) 
                    pq.updatePriority(old, (neighbour.getDistance(), neighbour))
                    
    def computeProperties(self, graph):
        if (graph.order > 0):
            #print("here")
            degrees = []
            edges = 0
            vertices = 0
            for v in graph:
                degrees.append(len(v.getNeighbours()))
                edges += 2*len(v.getNeighbours())
                vertices += 1
            edges = edges//2
            order = graph.order
            degrees.sort()
            maximumDegree = max(degrees)
            minimumDegree = min(degrees)
            if (maximumDegree == minimumDegree):
                regular = maximumDegree
            else:
                regular = None   
            properties = {}
            degreeSequence = tuple(degrees)
            properties["order"] = order
            properties["degree sequence"] = degreeSequence
            properties["min degree"] = minimumDegree
            properties["max degree"] = maximumDegree
            properties["num edges"] = edges
            properties["num vertices"] = vertices
            properties["regular"] = regular
            return properties
        
        
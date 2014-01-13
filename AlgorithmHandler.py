"""

{description}
    Copyright (C) {2014} {Karl Parkinson}

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

"""

import time

from tkinter import *
from Graph import Graph, DrawableGraph
from Vertex import Vertex, DrawableVertex
from PriorityQueue import PriorityQueue

class AlgorithmHandler:
    
    def __init__(self, canvas):
        self.canvas = canvas
        
        
    # Recursive version of depth first search
    def DFS(self, graph, start, canvas):
        start.setVisited(True)
        start.setColour("green")
        start.draw(canvas)
        canvas.update()
        time.sleep(0.5)
        for neighbour in start.getNeighbours():
            if (not neighbour.getVisited()):
                # Explore further
                self.DFS(graph, neighbour, canvas)  
    
    # Breadth first search
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
                    # Visit neighbour, add to queue
                    neighbour.setVisited(True)
                    neighbour.setColour("red")
                    neighbour.draw(surface)
                    surface.update()
                    time.sleep(0.5)
                    q.append(neighbour)  
    
    # Prim's algorithm for finding MST
    def prims(self, graph, start, canvas):
        for v in graph:
            v.setStatus(0)
            v.setParent(None)
                
        pq = PriorityQueue()
        pq.enQueue((0, start))
        while (not pq.isEmpty()):
            current = pq.deQueue()[1]
            current.setStatus(2)
            if(current.getParent() != None):
                graph.drawEdge(current.getParent(), current, canvas, "yellow")
                canvas.update()
                time.sleep(0.5)
            for neighbour in current.getNeighbours():
                if (neighbour.getStatus() == 0):  
                    # Encountered a new vertex
                    neighbour.setStatus(1)
                    neighbour.setParent(current)
                    neighbour.setpqWeight(current.neighbours[neighbour])
                    pq.enQueue((neighbour.getpqWeight(), neighbour))
                elif (neighbour.getStatus() == 1):
                    if (neighbour.getpqWeight() > current.neighbours[neighbour]):
                        # Found smaller weight, update accordingly
                        old = (neighbour.getpqWeight(), neighbour)
                        neighbour.setpqWeight(current.neighbours[neighbour])
                        pq.updatePriority(old, (neighbour.getpqWeight(), neighbour))
                        neighbour.setParent(current)
    
    # Dijkstra'a algorithm for finding shortest paths                 
    def dijkstras(self, graph, start, canvas):
        pq = PriorityQueue()
        for v in graph:
            v.setStatus(0)
            v.setDistance(float("inf"))
            pq.enQueue((v.getDistance(), v))
                    
        start.setDistance(0)
        pq.updatePriority((float("inf"), start), (0, start))
        for i in range(0, graph.order):
            current = pq.deQueue()[1]
            current.setStatus(2)
            if(current.getParent() != None):
                graph.drawEdge(current.getParent(), current, canvas, "blue")
                canvas.update()
                time.sleep(0.5)            
            for neighbour in current.getNeighbours():
                if (neighbour.getDistance()) > (current.getDistance() + current.neighbours[neighbour]):
                    # Found smaller weight, update accordingly.
                    old = (neighbour.getDistance(), neighbour)
                    neighbour.setParent(current)
                    neighbour.setDistance(current.getDistance() + current.neighbours[neighbour]) 
                    pq.updatePriority(old, (neighbour.getDistance(), neighbour))
                    
    # Compute the properties of the graph. Likely a better way to store than just 
    # jamming into a dictionary.
    def computeProperties(self, graph):
        if (graph.order > 0):
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
        
        
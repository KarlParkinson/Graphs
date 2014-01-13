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

import random

from tkinter import *

from Graph import Graph, DrawableGraph
from Vertex import Vertex, DrawableVertex
from AlgorithmHandler import AlgorithmHandler

"""
Responsible for handling events, mostly clicks. Adds vertices and edges.
Draws the graph afterwards.
"""

class EventHandler:
    
    def __init__(self, canvas):
        self.canvas = canvas
        self.startVertex = None
        self.endVertex = None
        self.startFound = False
        self.algorithmHandler = AlgorithmHandler(self.canvas)
        self.nextKey = 0
        
    # Create a new vertex, add to graph, draw graph.
    def newVertex(self, event, graph):
        vertex = DrawableVertex((event.x, event.y), self.nextKey)
        graph.addDrawableVertex(vertex)
        graph.drawGraph(self.canvas)
        self.nextKey += 1
        
    # Add edge, draw graph
    def newEdge(self, event, graph):
        for v in graph:
            if (v.clickedOn((event.x, event.y)) and not self.startFound):
                self.startFound = True
                self.startVertex = v
            elif(v.clickedOn((event.x, event.y)) and self.startFound):
                self.endVertex = v
                graph.addEdge(self.startVertex, self.endVertex, random.randint(0, 10))
                graph.drawGraph(self.canvas)
                self.startFound = False
                
    # Find start vertex, then call BFS in algHandler
    def handleDFS(self, graph, event):
        for v in graph:
            if(v.clickedOn((event.x, event.y))):
                startVertex = v
                for v in graph:
                    v.setVisited(False)
                self.algorithmHandler.DFS(graph, startVertex, self.canvas)
                return
    
    # Find start vertex, then call DFS in algHandler
    def handleBFS(self, graph, event):
        for v in graph:
            if(v.clickedOn((event.x, event.y))):
                self.algorithmHandler.BFS(graph, v, self.canvas)
                return
    
    # Find start vertex, then call Prims in algHandler        
    def handlePrims(self, graph, event):
        for v in graph:
            if(v.clickedOn((event.x, event.y))):
                self.algorithmHandler.prims(graph, v, self.canvas)
                return        
    
    # Find start vertex, then call Dijkstras in algHandler
    def handleDijkstra(self, graph, event):
        for v in graph:
            if(v.clickedOn((event.x, event.y))):
                self.algorithmHandler.dijkstras(graph, v, self.canvas)
                return    
    
    # Call properties function in algHandler        
    def handleProperties(self, graph):
        return self.algorithmHandler.computeProperties(graph)
        
    


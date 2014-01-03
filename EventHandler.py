import random

from tkinter import *

from Graph import Graph, DrawableGraph
from Vertex import Vertex, DrawableVertex
from AlgorithmHandler import AlgorithmHandler

"""
Responsible for handling events, mostly clicks
"""

class EventHandler:
    
    def __init__(self, canvas):
        self.canvas = canvas
        self.startVertex = None
        self.endVertex = None
        self.startFound = False
        self.algorithmHandler = AlgorithmHandler(self.canvas)
        
    def newVertex(self, event, graph):
        graph.addDrawableVertex((event.x, event.y), random.randint(0, 1000000))
        graph.drawGraph(self.canvas)
        
    def newEdge(self, event, graph):
        #print("New Edge")
        #print((event.x, event.y))
        for v in graph:
            #print("Yup")
            if (v.clickedOn((event.x, event.y)) and not self.startFound):
                #print("Here")
                self.startFound = True
                self.startVertex = v
            elif(v.clickedOn((event.x, event.y)) and self.startFound):
                #print("But")
                self.endVertex = v
                graph.addEdge(self.startVertex, self.endVertex, random.randint(0, 10))
                graph.drawGraph(self.canvas)
                self.startFound = False
                
    def handleDFS(self, graph, event):
        for v in graph:
            if(v.clickedOn((event.x, event.y))):
                startVertex = v
                for v in graph:
                    v.setVisited(False)
                self.algorithmHandler.DFS(graph, startVertex, self.canvas)
                return
            
    def handleBFS(self, graph, event):
        for v in graph:
            if(v.clickedOn((event.x, event.y))):
                self.algorithmHandler.BFS(graph, v, self.canvas)
                return
            
    def handlePrims(self, graph, event):
        for v in graph:
            if(v.clickedOn((event.x, event.y))):
                self.algorithmHandler.prims(graph, v, self.canvas)
                return        
        #self.algorithmHandler.prims(graph)
        
    def handleDijkstra(self, graph, event):
        for v in graph:
            if(v.clickedOn((event.x, event.y))):
                self.algorithmHandler.dijkstras(graph, v, self.canvas)
                return    
            
    def handleProperties(self, graph):
        return self.algorithmHandler.computeProperties(graph)
        
    

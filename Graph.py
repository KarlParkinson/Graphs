import pygame

from Vertex import Vertex
from Vertex import DrawableVertex
from pygame.locals import *


class Graph:
    def __init__(self):
        self.vertices = {}
        self.order = 0
    
    # Not a huge fan of this. Why would it return something?
    # Seems to me the vertex should already be made, shouldn't
    # be responsibility of graph to make vertices
    def addVertex(self, key):
        self.order += 1
        vertex = Vertex(key)
        self.vertices[key] = vertex
        return vertex
    
    def getVertex(self, n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None
        
    def __contains__(self, n):
        return n in self.vertices
    
    def addEdge(self, fromVertex, toVertex, cost=0):
        #if fromVertex not in self.vertices:
         #   vertex = self.addVertex(fromVertex)
        #if toVertex not in self.vertices:
         #   vertex = self.addVertex(toVertex)
        self.vertices[fromVertex.key].addNeighbour(self.vertices[toVertex.key], cost)
        # Without this, creates digraphs
        self.vertices[toVertex.key].addNeighbour(self.vertices[fromVertex.key], cost)
        
    def getVertices(self):
        return self.vertices.keys()
    
    def __iter__(self):
        return iter(self.vertices.values())
    
    def printGraph(self):
        for vertex in self.vertices.keys():
            print(self.vertices[vertex])
            #print(str(vertex.getId()) + " connected to: " + str([x.id for x in vertex.getNeighbours()]))
            
    #def printEdges(self):
     #   for vertex in self.vertices:
      #      print(vertex)
       #     edges = v.getNeighbours()
        #    for e in edges:
       
       
class DrawableGraph(Graph):
    def __init__(self):
        super().__init__()
        #self.font = pygame.font.SysFont('default', 10)
        
    def addDrawableVertex(self, center, key):
        self.order += 1
        vertex = DrawableVertex(center, key)
        self.vertices[key] = vertex
        return vertex
        
    def drawGraph(self, surface):
        for v in self.vertices.keys():
            self.vertices[v].draw(surface)
        for v in self.vertices.keys():
            start = self.vertices[v]
            for n in start.getNeighbours():
                self.drawEdge(start, n, surface, "black")

                
    def drawEdge(self, start, end, surface, color):
        pygame.draw.line(surface, pygame.Color(color), start.center, end.center)
        half = ((start.center[0]+end.center[0])/2, (start.center[1]+end.center[1])/2)
        font = pygame.font.SysFont('default', 25)
        blitSurface = font.render(str(start.neighbours[end]), True, pygame.Color("black"))
        surface.blit(blitSurface, half)
        pygame.display.update()
                
            

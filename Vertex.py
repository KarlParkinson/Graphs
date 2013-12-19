import pygame

from pygame.locals import *

class Vertex:
    def __init__(self, key):
        self.key = key
        self.neighbours = {}
        self.visited = False

    
    def addNeighbour(self, nbr, weight=0):
        self.neighbours[nbr] = weight
        
    
    def getNeighbours(self):
        return self.neighbours.keys()

    
    def getId(self):
        return self.key
    

    def getWeight(self, nbr):
        return self.neighbours[nbr]
    
    def __str__(self):
        return str(self.key) + " connected to: " + str([x.key for x in self.neighbours])
    
    def getVisited(self):
        return self.visited
    
    def setVisited(self, value):
        self.visited = value
        

"""
Vertex that can be used with a graphics library (in this case, python). Adds a center, radius, colour, and draw methods
"""
class DrawableVertex(Vertex):
    def __init__(self, center, key):
        super().__init__(key)
        self.center = center
        self.radius = 10
        self.colour = "black"
        self.key = key
        
    def draw(self, surface):
        pygame.draw.circle(surface, pygame.Color(self.colour), self.center, self.radius)
        
    def setColour(self, colour):
        self.colour = colour
        
    def setVisited(self, value, colour):
        self.visited = value
        self.setColour(colour)
        
    def clickedOn(self, pos):
        if (((pos[0]-self.center[0])**2 + (pos[1]-self.center[1])**2) <= self.radius):
            return True
        else:
            return False
        
    
    
    

        
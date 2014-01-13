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

from tkinter import *

class Vertex:
    def __init__(self, key):
        self.key = key
        self.neighbours = {}
        self.visited = False
        self.status = 0
        self.parent = None
        self.distance = None
        self.pqWeight = None

    
    def addNeighbour(self, nbr, weight=0):
        self.neighbours[nbr] = weight
        
    
    def getNeighbours(self):
        return self.neighbours.keys()

    
    def getId(self):
        return self.key
    
    def setpqWeight(self, weight):
        self.pqWeight = weight
        
    def getpqWeight(self):
        return self.pqWeight

    def getWeight(self, nbr):
        return self.neighbours[nbr]
    
    def __str__(self):
        return str(self.key) + " connected to: " + str([x.key for x in self.neighbours])
    
    def getVisited(self):
        return self.visited
    
    def setVisited(self, value):
        self.visited = value
        
    def setStatus(self, status):
        self.status = status
        
    def getStatus(self):
        return self.status
        
    def setParent(self, parent):
        self.parent = parent
        
    def getParent(self):
        return self.parent
    
    def getDistance(self):
        return self.distance
    
    def setDistance(self, distance):
        self.distance = distance
        
    def __lt__(self, other):
        return other
        


# Vertex that can be used with a graphics library (in this case, tkinter). Adds a center, radius, colour, and draw methods
class DrawableVertex(Vertex):
    def __init__(self, center, key):
        super().__init__(key)
        self.center = center
        self.radius = 10
        self.colour = "black"
        self.key = key
        
    def draw(self, surface):
        surface.create_oval(self.center[0]-self.radius, self.center[1]-self.radius, self.center[0]+self.radius, self.center[1]+self.radius, fill=self.colour)
        
    def setColour(self, colour):
        self.colour = colour
        
    def setVisited(self, value):
        self.visited = value
        
    def clickedOn(self, pos):
        if (((pos[0]-self.center[0])**2 + (pos[1]-self.center[1])**2) <= self.radius):
            return True
        else:
            return False
        
    
    
    

        
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

"""
Implementation of a Graph using adjacency list
"""

from Vertex import Vertex
from Vertex import DrawableVertex
from tkinter import *


class Graph:
    def __init__(self):
        self.vertices = {}
        self.order = 0
    
    def addVertex(self, vertex):
        self.order += 1
        self.vertices[vertex.getId()] = vertex
    
    def getVertex(self, n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None
        
    def __contains__(self, n):
        return n in self.vertices
    
    def addEdge(self, fromVertex, toVertex, cost=0):
        if (fromVertex != toVertex):
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
            
       
# Graph that can be used with a graphics library
class DrawableGraph(Graph):
    def __init__(self):
        super().__init__()

        
    def addDrawableVertex(self, vertex):
        self.order += 1
        self.vertices[vertex.getId()] = vertex
        
    def drawGraph(self, canvas):
        for v in self.vertices.keys():
            self.vertices[v].draw(canvas)
        for v in self.vertices.keys():
            start = self.vertices[v]
            for n in start.getNeighbours():
                self.drawEdge(start, n, canvas, "black")

               
    def drawEdge(self, start, end, surface, color):
        a = start.center[0]
        b = start.center[1]
        c = end.center[0]
        d = end.center[1]
        surface.create_line(a, b, c, d, fill=color)
        half = ((start.center[0]+end.center[0])/2, (start.center[1]+end.center[1])/2)
        surface.create_text(half[0], half[1], text=str(start.neighbours[end]), anchor=NE)

           

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
The GUI interface. Displays the graph, options, and interacts with the user.
"""

import random
import time

from tkinter import messagebox

from tkinter import *
from Graph import Graph, DrawableGraph
from Vertex import Vertex, DrawableVertex
from EventHandler import EventHandler
from PropertiesDialog import PropertiesDialog


class App:
    
    def __init__(self):
        self.root = Tk()
        
        self.setUpMenu()
        
        self.canvas = self.setUpCanvas(self.root, 800, 800)
        self.canvas.pack()
        self.graph = DrawableGraph ()
        
        self.eventHandler = EventHandler(self.canvas)
        self.root.mainloop()
        
    def setUpMenu(self):
        menubar = Menu(self.root)
        menubar.add_command(label="New Graph", command=self.newGraph)
        menubar.add_command(label="Properties", command=self.properties)
        menubar.add_command(label="Reset Graph", command = self.resetGraph)
        
        algMenu = Menu(menubar, tearoff=0)
        algMenu.add_command(label="Depth First Search", command=self.dfs)
        algMenu.add_command(label="Breadth First Search", command=self.bfs)
        algMenu.add_command(label="Prim's Algorithm", command=self.prims)
        algMenu.add_command(label="Dijkstra's Algorithm", command=self.dijkstras)
        menubar.add_cascade(label="Algorithms", menu=algMenu)
        
        addMenu = Menu(menubar, tearoff=0)
        addMenu.add_command(label="Vertices", command=self.addVertices)
        addMenu.add_command(label="Edges", command=self.addEdges)
        menubar.add_cascade(label="Add", menu=addMenu)
        self.root.config(menu=menubar)        
        
    # Bind mouse click event to add a new vertex
    def addVertices(self):
        messagebox.showinfo("Add Vertex", "Click anywhere to add a vertex")
        self.canvas.bind("<Button-1>", self.newVertex)
    
    # Bind mouse click event to add a new edge    
    def addEdges(self):
        messagebox.showinfo("Add Edge", "Select a start vertex and an end vertex")
        self.canvas.bind("<Button-1>", self.newEdge)
        
    # Wipe canvas, set graph attribute to a new graph
    def newGraph(self):
        self.canvas.delete("all")
        self.graph = DrawableGraph()
        self.canvas.unbind("<Button-1>")
        
    # Colour all edges and vertices black
    def resetGraph(self):
        for v in self.graph:
            v.setColour("black")
        self.graph.drawGraph(self.canvas)
        
    # Tell eventHandler to add a new edge
    def newEdge(self, event):
        self.eventHandler.newEdge(event, self.graph)
    
    # Get properties back from eventHandler and display
    def properties(self):
        properties = self.eventHandler.handleProperties(self.graph) 
        # Graph has no edges or vertices, so do not show anything
        if (properties != None):
            PropertiesDialog(self.root, properties)
        
     # Bind mouse click event to DFS  
    def dfs(self):
        messagebox.showinfo("DFS", "Click on a start vertex")
        self.canvas.bind("<Button-1>", self.handleDFS)
        
    def handleDFS(self, event):
        self.eventHandler.handleDFS(self.graph, event)
    
    # Bind mouse click event to BFS
    def bfs(self):
        messagebox.showinfo("BFS", "Click on a start vertex")
        self.canvas.bind("<Button-1>", self.handleBFS)
        
    def handleBFS(self, event):
        self.eventHandler.handleBFS(self.graph, event)
    
    # Bind mouse click event to Prims
    def prims(self):
        messagebox.showinfo("Prims", "Click on a start vertex")
        self.canvas.bind("<Button-1>", self.handlePrims)
        
    def handlePrims(self, event):
        self.eventHandler.handlePrims(self.graph, event)
        
    # Bind mouse click event to Dijkstras
    def dijkstras(self):
        messagebox.showinfo("Dijkstras", "Click on a start vertex")
        self.canvas.bind("<Button-1>", self.handleDijkstra)
        
    def handleDijkstra(self, event):
        self.eventHandler.handleDijkstra(self.graph, event)
        
    def draw(self):
        self.graph.drawGraph(self.canvas)
        
    def setUpCanvas(self, master, width, height):
        canvas = Canvas(master, width=width, height=height)
        return canvas
    
    def newVertex(self, event):
        self.eventHandler.newVertex(event, self.graph)
      
      
      
def main():
    app = App()


    
if __name__ == "__main__":
    main()
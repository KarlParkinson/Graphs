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
        
    def addVertices(self):
        self.canvas.bind("<Button-1>", self.newVertex)
        
    def addEdges(self):
        self.canvas.bind("<Button-1>", self.newEdge)
        
    def newGraph(self):
        self.canvas.delete("all")
        self.graph = DrawableGraph()
        self.canvas.unbind("<Button-1>")
        
    def resetGraph(self):
        for v in self.graph:
            v.setColour("black")
        self.graph.drawGraph(self.canvas)
        
    def newEdge(self, event):
        self.eventHandler.newEdge(event, self.graph)
        
    def properties(self):
#        print(self.graph.order)
        properties = self.eventHandler.handleProperties(self.graph)
  #      print(properties)
        PropertiesDialog(self.root, properties)
        
        
    def dfs(self):
        messagebox.showinfo("DFS", "Click on a start Vertex")
        self.canvas.bind("<Button-1>", self.handleDFS)
        
    def handleDFS(self, event):
        #print("TTTT")
        self.eventHandler.handleDFS(self.graph, event)
        
    def bfs(self):
        messagebox.showinfo("BFS", "Click on a start Vertex")
        self.canvas.bind("<Button-1>", self.handleBFS)
        
    def handleBFS(self, event):
        self.eventHandler.handleBFS(self.graph, event)
        
    def prims(self):
        #print("Prims")
        self.canvas.bind("<Button-1>", self.handlePrims)
        #self.eventHandler.handlePrims(graph)
        
    def handlePrims(self, event):
        self.eventHandler.handlePrims(self.graph, event)
        
    def dijkstras(self):
        #print("Dijkstra")
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
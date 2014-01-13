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
The dialog box to display the properties of the graph
"""

from tkinter import *
import os

class PropertiesDialog(Toplevel):
    
    def __init__(self, parent, properties, title=None):
        Toplevel.__init__(self, parent)
        self.transient(parent)
        
        self.properties = properties
        
        if title:
            self.title(title)
        
        self.parent = parent
        
        self.result = None
        
        body = Frame(self)
        self.initial_focus = self.body(body)
        body.pack(padx=5, pady=5)
        
        
        self.grab_set()
        
        if not self.initial_focus:
            self.initial_focus = self
        
        self.protocol("WM_DELETE_WINDOW", self.cancel)
        
        self.geometry("+%d+%d" % (parent.winfo_rootx()+50, parent.winfo_rooty()+50))
        
        
        self.wait_window(self)
        
    def buttonbox(self):
        box = Frame(self)
    
        w = Button(box, text="OK", width=10, command=self.ok, default=ACTIVE)
        w.pack(side=LEFT, padx=5, pady=5)
        w = Button(box, text="Cancel", width=10, command=self.cancel)
        w.pack(side=LEFT, padx=5, pady=5)
    
        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)
    
        box.pack()
    
    
    def ok(self, event=None):
    
        if not self.validate():
            self.initial_focus.focus_set() # put focus back
            return
    
        self.withdraw()
        self.update_idletasks()
    
        self.apply()
    
        self.cancel()
    
    def cancel(self, event=None):
    
        # put focus back to the parent window
        self.parent.focus_set()
        self.destroy()
    
    
    def validate(self):
        pass
    
    def apply(self):
        pass       
    
    # Format output
    def body(self, master):
        
        Label(master, text="Order: " + str(self.properties["order"])).grid(row=0)
        Label(master, text="Degree Sequence: " + str(self.properties["degree sequence"])).grid(row=1)
        Label(master, text="Minimum Degree: " + str(self.properties["min degree"])).grid(row=2)
        Label(master, text="Maximum Degree: " + str(self.properties["max degree"])).grid(row=3)
        Label(master, text="Edges: " + str(self.properties["num edges"])).grid(row=4)
        Label(master, text="Vertices: " + str(self.properties["num vertices"])).grid(row=5)
        if (self.properties["regular"] == None):
            Label(master, text="Regular: No").grid(row=6)
        else:
            Label(master, text="Regular: " + str(self.properties["regular"])).grid(row=6)
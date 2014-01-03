from tkinter import *
import simpleDialog

class WeightDialog(simpleDialog.Dialog):
    

    def body(self, master):
        self.r1 = Radiobutton(master, text="Random Weights", variable=self.result, value=0).pack()
        self.r2 = Radiobutton(master, text="Custom Weights", variable=self.result, value=1).pack()
        self.r3 = Radiobutton(master, text="No Weights", variable=self.result, value=None).pack()
        

        #Label(master, text="First:").grid(row=0)
        #Label(master, text="Second:").grid(row=1)

        #self.e1 = Entry(master)
        #self.e2 = Entry(master)

        #self.e1.grid(row=0, column=1)
        #self.e2.grid(row=1, column=1)
        return self.r1 # initial focus

    def apply(self):
        print(self.result)
        #first = int(self.e1.get())
        #second = int(self.e2.get())
        #self.result = (first, second) # or something
        
        
root = Tk()
Button(root, text="Hello!").pack()
root.update()
        
d = WeightDialog(root)

root.wait_window(d.parent)
print(d.result)
root.mainloop()     
#root.wait_window(d.top)
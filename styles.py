from tkinter import ttk

class Styles:
    def __init__(self):
        self.s = ttk.Style()

    @property
    def separatorStyle(self):
        name = "Separator.TSeparator"
        self.s.configure(name,
                    color="black",
                    orient="vertical",
                    width=5)
        return name
    
    @property
    def baseFrame(self):
        name = "BaseFrame.TFrame"
        self.s.configure(name,
                    width=100,
                    background="white",
                    borderwidth=2)
        return name
    
    @property
    def greenFrame(self):
        name = "GreenFrame.TFrame"
        self.s.configure(name,
                    background="green",
                    borderwidth=2)
        return name
    
    @property
    def redFrame(self):
        name = "RedFrame.TFrame"
        self.s.configure(name,
                    width=100,
                    background="red",
                    borderwidth=2)
        return name
    
    @property
    def blueFrame(self):
        name = "BlueFrame.TFrame"
        self.s.configure(name,
                    background="blue",
                    borderwidth=2)
        return name
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
                    background="white")
        return name
    
    @property
    def iconFrame(self):
        name = "IconFrame.TFrame"
        self.s.configure(name,
                    background="white")
        return name

    @property
    def label(self):
        name = "Label.TLabel"
        self.s.configure(name,
                    background="white",
                    font=("Arial", 14))
        return name
    
    @property
    def imgLabel(self):
        name = "ImageLabel.TLabel"
        self.s.configure(name,
                    background="white",
                    borderwidth=2)
        return name
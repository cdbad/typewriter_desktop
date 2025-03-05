import os
import tkinter as tk
# from screeninfo import get_monitors
from keybindings import Bindings
from UI.home import UI
from dotenv import load_dotenv
from os import listdir

load_dotenv()


class Home(tk.Tk, Bindings, UI):
    def __init__(self, *args, **kwargs):
        # monitor = get_monitors()[0]

        self.SSD_PATH = os.getenv("SSD_PATH")
        self.ICON_PATH = os.getenv("ICON_PATH")
        self.width = 800
        self.height = 480

        self.filenames = listdir(self.SSD_PATH)
        self.files = {f"{f}": {"img": None, "ref": None} for f in self.filenames}

        tk.Tk.__init__(self)
        self.geometry(f"{self.width}x{self.height}")
        self.configure(bg="white")
        # self.attributes("-fullscreen", True)
        # self.attributes("-type", "splash")
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.grid_propagate(False)

        self.draw_home()
        self.bindings()


if __name__ == "__main__":
    app = Home()
    app.mainloop()

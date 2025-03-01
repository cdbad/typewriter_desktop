import os
import tkinter as tk
from screeninfo import get_monitors
from keybindings import Bindings
from UI.home import UI
from dotenv import load_dotenv

load_dotenv()

class Home(tk.Tk, Bindings, UI):
    def __init__(self, *args, **kwargs):
        monitor = get_monitors()[0]

        self.SSD_PATH = os.getenv("SSD_PATH")
        self.ICON_PATH = os.getenv("ICON_PATH")
        self.width = monitor.width
        self.height = monitor.height

        tk.Tk.__init__(self)
        self.geometry(f"{self.width}x{self.height}")
        self.configure(bg="white")
        self.attributes("-fullscreen", True)
        self.attributes("-type", "splash")

        self.draw_home()
        self.bindings()


if __name__ == "__main__":
    app = Home()
    app.mainloop()

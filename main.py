import tkinter as tk
from screeninfo import get_monitors
from keys import Bindings
from UI import UI
from styles import Styles


class Home(tk.Tk, Bindings, UI, Styles):
    def __init__(self, *args, **kwargs):
        monitor = get_monitors()[0]
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

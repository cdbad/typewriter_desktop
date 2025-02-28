from tkinter import ttk
from styles import Styles


class UI():
    def draw_home(self):
        self.styles = Styles()

        # Menu
        self.menu = ttk.Frame(self,
                              borderwidth=1,
                              width=100,
                              height=self.height,
                              style=self.styles.baseFrame)
        self.menu.grid(column=0, row=0, sticky="ws")

        # Separator
        self.separator = ttk.Separator(
            self,
            orient="vertical",
            style=self.styles.separatorStyle
        ).grid(column=1, row=0, sticky="ns", pady=45)

        # Files
        self.files = ttk.Frame(self,
                               borderwidth=1,
                               width=self.width-100,
                               height=self.height,
                               style=self.styles.baseFrame)
        self.files.grid(column=2, row=0, sticky="swen")

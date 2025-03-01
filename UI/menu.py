from tkinter import ttk

class Menu():
    def draw_menu(self):
        self.menu = ttk.Frame(self,
                            borderwidth=1,
                            width=100,
                            height=self.height,
                            style=self.styles.baseFrame)
        self.menu.grid(column=0, row=0, sticky="ws")
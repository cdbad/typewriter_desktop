from tkinter import ttk
from PIL import Image, ImageTk


class Menu():
    def draw_menu(self):
        self.menu = ttk.Frame(self,
                            borderwidth=1,
                            width=100,
                            height=self.height,
                            style=self.styles.baseFrame)
        self.menu.pack_propagate(False)
        
        # img = Image.open(self.ICON_PATH + "settings-icon.png")
        # img = img.resize((20, 20))
        # img = ImageTk.PhotoImage(img)
        # self.settings_icon = ttk.Label(self.menu,
        #                             image=img,
        #                             style=self.styles.imgLabel)
        # self.settings_icon.pack()

        self.menu.grid(column=0, row=0, sticky="ns")
from tkinter import ttk
from .styles import Styles
from .menu import Menu
from .file_manager import FileManager
from .separator import Separator


class UI(Menu, FileManager, Separator):
    def draw_home(self):
        self.styles = Styles()

        # self.main_frame = ttk.Frame(self,
        #                             width=self.width,
        #                             height=self.height,
        #                             style=self.styles.baseFrame)
        # self.rowconfigure(0, weight=1)
        # self.rowconfigure(1, weight=1)
        # self.rowconfigure(2, weight=1)

        # Menu
        self.draw_menu()

        # Separator
        self.draw_separator()

        # Files
        self.draw_files()

        # self.main_frame.pack(fill="both")

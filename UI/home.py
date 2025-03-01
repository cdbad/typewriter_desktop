from tkinter import ttk
from .styles import Styles
from .menu import Menu
from .file_manager import FileManager


class UI(Menu, FileManager):
    def draw_home(self):
        self.styles = Styles()

        # Menu
        self.draw_menu()

        # Separator
        self.separator = ttk.Separator(
            self,
            orient="vertical",
            style=self.styles.separatorStyle
        ).grid(column=1, row=0, sticky="ns", pady=45)

        # Files
        self.draw_files()

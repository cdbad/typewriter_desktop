from os import listdir
from PIL import Image, ImageTk
from tkinter import ttk


class FileManager:
    def draw_files(self):
        self.filenames = listdir(self.SSD_PATH)

        self.files = ttk.Frame(self,
                               borderwidth=1,
                               width=self.width-100,
                               height=self.height,
                               style=self.styles.baseFrame)

        self.icon_refs = []
        for i, file in enumerate(self.filenames):
            self.icon_refs.append(self.select_image(file.split(".")[1]))

            icon_frame = ttk.Frame(self.files,
                                   style=self.styles.iconFrame)

            image_label = ttk.Label(icon_frame,
                                    image=self.icon_refs[i],
                                    style=self.styles.imgLabel)
            image_label.pack()

            file_label = ttk.Label(icon_frame,
                                  text=file.split(".")[0],
                                  style=self.styles.label)
            file_label.pack()

            icon_frame.grid(column=i, row=0, sticky="w", padx=10, pady=20)
            i += 1

        self.files.grid(column=2, row=0, sticky="swen", padx=45, pady=25)
    
    def select_image(self, extension):
        if extension == "odt":
            img = Image.open(self.ICON_PATH + "odt-icon.png")
            img = img.resize((100, 100))
            img = ImageTk.PhotoImage(img)
            return img
from PIL import Image, ImageTk
from tkinter import ttk
from .focus_setter import set_focus


class FileManager:
    def draw_files(self):
        self.files_frame = ttk.Frame(self,
                               width=self.width-100,
                               height=self.height,
                               style=self.styles.baseFrame)
        self.files_frame.pack_propagate(False)

        for i, file in enumerate(self.filenames):
            img_ref = self.select_image(file.split(".")[1])
            
            self.files[file]["img"] = img_ref

            icon_frame = ttk.Frame(self.files_frame,
                                   style=self.styles.iconFrame)
            self.files[file]["ref"] = icon_frame

            image_label = ttk.Label(icon_frame,
                                    image=self.files[file]["img"],
                                    style=self.styles.imgLabel)
            image_label.pack()

            file_label = ttk.Label(icon_frame,
                                  text=file.split(".")[0],
                                  style=self.styles.label)
            file_label.pack()

            icon_frame.grid(column=i, row=0, sticky="w", padx=20, pady=20)
            i += 1

        self.files_frame.grid(column=2, row=0, sticky="swen", padx=45, pady=25)

        if len(self.filenames) > 0:
            set_focus(self.files[self.filenames[0]]["ref"])
    
    def select_image(self, extension):
        if extension == "odt":
            img = Image.open(self.ICON_PATH + "odt-icon.png")
        elif extension == "txt":
            img = Image.open(self.ICON_PATH + "txt-icon.png")
        elif extension == "docx":
            img = Image.open(self.ICON_PATH + "docx-icon.png")

        img = img.resize((45, 45))
        img = ImageTk.PhotoImage(img)
        return img
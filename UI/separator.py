from tkinter import ttk
# from wrapper import wrapper


class Separator:
    def draw_separator(self):
        frame_wrapper = ttk.Frame(self)
        frame_wrapper.pack_propagate(False)

        self.separator_frame = ttk.Frame(frame_wrapper,
                                         style=self.styles.testFrame,
                                         height=self.height,
                                         width=10)

        self.separator = ttk.Separator(
            self.separator_frame,
            orient="vertical",
            style=self.styles.separatorStyle
        ).pack(fill="y")
        
        self.separator_frame.pack(fill="y")

        frame_wrapper.grid(column=1, row=0, sticky="ns", pady=45)
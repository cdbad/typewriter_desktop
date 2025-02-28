class Bindings:
    def bindings(self):
        self.bind("<Escape>", lambda event: self.destroy())
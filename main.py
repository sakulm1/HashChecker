import tkinter as tk
from hashChecker import HashChecker 

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('500x500')
        self.menuFrame = tk.Frame(self, bg="pink", width=130)
        self.menuFrame.pack(side="left", fill="y")

        self.contentFrame = tk.Frame(self, bg="red")
        self.contentFrame.pack(side="right", fill="both", expand=True)

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=5)



if __name__ == "__main__":
    app = App()
    app.mainloop()
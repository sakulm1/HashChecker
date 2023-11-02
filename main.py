import tkinter as tk
from hashChecker import HashWindow 

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('500x500')
        self.title("Beta")
        self.menuFrame = tk.Frame(self, bg="pink", width=130)
        self.menuFrame.pack(side="left", fill="y")
        
        self.HashWindow = HashWindow()
        self.contentFrame = self.HashWindow.show()
        self.contentFrame.pack(side="right", fill="both", expand=True)


class Test(tk.Frame):
    def __init__(self):
        self.frame = tk.Frame()
        self.Lable = tk.Label(self.frame, text="test")
        self.Lable.pack()

    def show(self):
        return self.frame


if __name__ == "__main__":
    app = App()
    app.mainloop()
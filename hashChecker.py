import itertools
import hashlib
import tkinter as tk
import threading
test = "4dcc4173d80a2817206e196a38f0dbf7850188f, 44d5369032336a51fe00c7ad691c6d370cd91c90, df44a1c6f830f3230610f6812231585f7b883859, a3a882f4860f09e8f8b526ba15a161951ef7a00f, 1a359101fcc11d2d3864d2d423d8e6dd1c6d82ca, 74375d47cac9acd5a22df9625773d5e071453e8e, 765750e41995b3b0b79d491b39dd5c04db97cb73"
hashes = []
characters = " abcdefghijklmnopqrstuvwxyz"
#characters = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!§$%&/()=?äöüß+-#*~,.;:<>|{}[]"
max_password_length = 1

class hashCreator:
    isGenerating = False
    countFound = 0
    def __init__(self, hashes, characters, password_length) -> None:
        self.hashes = hashes
        self.characters = characters
        self.password_length = password_length

    def __sha1hex(self, sha1in: str):
        return hashlib.sha1(sha1in.encode('utf-8')).hexdigest()
    
    def start(self):
        self.isGenerating = True
        th = threading.Thread(target=self.newThread)
        th.start()
         
    def newThread(self):
        for length in range(1, self.password_length + 1):
            self.kombinationen(length)

    def stop(self):
        self.isGenerating = False
    
    def kombinationen(self, length):
        for combination in itertools.product(self.characters, repeat=length):
            password = ''.join(combination)
            password_sha1 = self.__sha1hex(password)
            if password_sha1 in self.hashes:
                o = f"Found Password {password}, Hash -> {password_sha1}"
                app.foundPasswords.insert(self.countFound, f"Password {password} -> {password_sha1}")
            print(f"{password} -> {password_sha1}")
            if not self.isGenerating: return


class App(tk.Tk):
    generator = hashCreator(hashes, characters, max_password_length)
    countHashes = 0
    def __init__(self):
        super().__init__()
        
        self.title = tk.Label(text="Hash Checker")
        self.title.grid(row=0, column=0, sticky="ew")

        self.btnStart = tk.Button(self, text="Start", command=self.generator.start)
        self.btnStart.grid(row=1, column=0, sticky="ew")

        self.btnStop = tk.Button(self, text="Stop", command=self.generator.stop)
        self.btnStop.grid(row=1, column=1, sticky="ew")

        self.btnClear = tk.Button(self, text="Clear", command=self.clearList)
        self.btnClear.grid(row=1, column=2, sticky="ew")

        self.foundPasswords = tk.Listbox(self)
        self.foundPasswords.grid(row=2, column=0, columnspan=3, sticky="ew")

        self.passwordLable = tk.Label(self, text="Max Length: ")
        self.passwordLable.grid(row=3, column=0, sticky="ew")
        self.passwordLength = tk.Entry(self)
        self.passwordLength.grid(row=3, column=1, sticky="ew")
        self.safeLen = tk.Button(self, text="ok", command=self.saveLen)
        self.safeLen.grid(row=3, column=2, sticky="ew")

        self.checkHashesLable = tk.Label(self, text="Hashes to check:")
        self.checkHashesLable.grid(row=4, column=0, sticky="ew")
        self.checkHashesEntry = tk.Entry(self)
        self.checkHashesEntry.grid(row=4, column=1, sticky="ew")
        self.checkHashesBtn = tk.Button(self, text="Add", command=self.addCheckHash)
        self.checkHashesBtn.grid(row=4, column=2, sticky="ew")
        self.checkHashesList = tk.Listbox(self)
        self.checkHashesList.grid(row=5, column=0, columnspan=3, sticky="ew")

        self.statusBar = tk.Frame(self, bg="green", height=20, width=self.winfo_width())
        self.statusBar.grid(row=6, column=0, columnspan=3, sticky="w")

    def saveLen(self):
        try:
            value = int(self.passwordLength.get())
            self.generator.password_length = int(value)
            print(self.generator.password_length)
        except ValueError:
            print("not a valid integer 😔")

    def addCheckHash(self):
        value = str(self.checkHashesEntry.get())
        if "," in value:
            values = value.split(", ")
            for text in values:
                text.strip()
                self.addListItem(text)
        else:
            self.addListItem(value)
        self.checkHashesEntry.delete(0, 'end')

    def addListItem(self, text):
        self.generator.hashes.append(text)
        self.checkHashesList.insert(self.countHashes, text)
        self.countHashes += 1
    
    def clearList(self):
        self.foundPasswords.delete(0, 'end')
        self.checkHashesList.delete(0, 'end')
        self.generator.hashes.clear()
        

if __name__ == "__main__":
    app = App()
    app.mainloop()







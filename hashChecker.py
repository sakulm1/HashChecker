import itertools
import hashlib
import tkinter as tk
import threading
test = "4dcc4173d80a2817206e196a38f0dbf7850188f, 44d5369032336a51fe00c7ad691c6d370cd91c90, df44a1c6f830f3230610f6812231585f7b883859, a3a882f4860f09e8f8b526ba15a161951ef7a00f, 1a359101fcc11d2d3864d2d423d8e6dd1c6d82ca, 74375d47cac9acd5a22df9625773d5e071453e8e, 765750e41995b3b0b79d491b39dd5c04db97cb73"
hashes = []
characters = " "
#characters = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!§$%&/()=?äöüß+-#*~,.;:<>|{}[]"
max_password_length = 1

class HashChecker:
    isGenerating = False
    countFound = 0
    def __init__(self, hashes, characters, password_length, hash_window) -> None:
        self.hashes = hashes
        self.characters = characters
        self.password_length = password_length
        self.hash_window = hash_window

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

    def calcTrys(self):
        total_combinations = 1
        for length in range(1, self.password_length + 1):
            total_combinations += len(self.characters) ** length

        return total_combinations

    def kombinationen(self, length):
        for combination in itertools.product(self.characters, repeat=length):
            password = ''.join(combination)
            password_sha1 = self.__sha1hex(password)
            if password_sha1 in self.hashes:
                self.hash_window.foundPasswords.insert(self.countFound, f"Password {password} -> {password_sha1}")
            #print(f"{password} -> {password_sha1}")
            self.hash_window.addOutput(f"{password} -> {password_sha1}")  # Verwenden Sie self.hash_window
            if not self.isGenerating: return


class HashWindow(tk.Frame):
    #generator = HashChecker(hashes, characters, max_password_length, self)
    countHashes = 0
    countTrys = 0
    def __init__(self):
        #super().__init__()
        self.generator = HashChecker(hashes, characters, max_password_length, self) 

        self.rFrame = tk.Frame() #return Frame

        self.title = tk.Label(self.rFrame, text="Hash Checker")
        self.title.grid(row=0, column=0, sticky="ew")

        self.btnStart = tk.Button(self.rFrame, text="Start",foreground="green", command=self.generator.start)
        self.btnStart.grid(row=1, column=0, sticky="ew")

        self.btnStop = tk.Button(self.rFrame, text="Stop", foreground="red", command=self.generator.stop,)
        self.btnStop.grid(row=1, column=1, sticky="ew")

        self.btnClear = tk.Button(self.rFrame, text="Clear", command=self.clearList)
        self.btnClear.grid(row=1, column=2, sticky="ew")

        self.foundPasswords = tk.Listbox(self.rFrame)
        self.foundPasswords.grid(row=2, column=0, columnspan=3, sticky="ew")

        self.passwordLabel = tk.Label(self.rFrame, text="Max Length: ")
        self.passwordLabel.grid(row=3, column=0, sticky="ew")
        self.passwordLength = tk.Entry(self.rFrame)
        self.passwordLength.grid(row=3, column=1, sticky="ew")
        self.safeLen = tk.Button(self.rFrame, text="Ok", command=self.saveLen)
        self.safeLen.grid(row=3, column=2, sticky="ew")

        self.checkHashesLable = tk.Label(self.rFrame, text="Hashes to check:")
        self.checkHashesLable.grid(row=4, column=0, sticky="ew")
        self.checkHashesEntry = tk.Entry(self.rFrame)
        self.checkHashesEntry.grid(row=4, column=1, sticky="ew")
        self.checkHashesBtn = tk.Button(self.rFrame, text="Add", command=self.addCheckHash)
        self.checkHashesBtn.grid(row=4, column=2, sticky="ew")

        self.separator1 = tk.Frame(self.rFrame, height=3, bg="gray")
        self.separator1.grid(row=5, column=0, columnspan=3, sticky="ew")
        self.titleCheckHash = tk.Label(self.rFrame, text="Looking for these hashes:")
        self.titleCheckHash.grid(row=6, column=0, columnspan=3, sticky="ew")

        self.checkHashesList = tk.Listbox(self.rFrame)
        self.checkHashesList.grid(row=7, column=0, columnspan=3, sticky="ew")

        self.separator2 = tk.Frame(self.rFrame, height=3, bg="gray")
        self.separator2.grid(row=8, column=0, columnspan=3, sticky="ew")
        self.titleOutput = tk.Label(self.rFrame, text="Output:")
        self.titleOutput.grid(row=9, column=0, columnspan=3, sticky="ew")
        self.output = tk.Listbox(self.rFrame)
        self.output.grid(row=10, column=0, columnspan=3, sticky="ew")

        self.charactersLabel = tk.Label(self.rFrame, text="Characters: ")
        self.charactersLabel.grid(row=11, column=0, sticky="ew")
        self.charactersEntry = tk.Entry(self.rFrame)
        self.charactersEntry.grid(row=11, column=1, sticky="ew")
        self.charactersButton = tk.Button(self.rFrame, text="OK", command=self.saveCharacters)
        self.charactersButton.grid(row=11, column=2, sticky="ew")

        self.setCharacters()
    
    def show(self):
        return self.rFrame

    def saveCharacters(self):
        text = self.charactersEntry.get()
        self.generator.characters = text

    def setCharacters(self):
        characters = " abcdefghijklmnopqrstuvwxyz"
        self.charactersEntry.insert(0, characters)
        self.generator.characters = characters

    def saveLen(self):
        try:
            value = int(self.passwordLength.get())
            self.generator.password_length = int(value)
            maxCombination = self.generator.calcTrys()
            print(maxCombination)
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
        self.output.delete(0, 'end')
        self.generator.hashes.clear()
        self.countHashes = 0
        self.countTrys = 0

    def addOutput(self, text):
        self.output.insert(self.countTrys, text)
        








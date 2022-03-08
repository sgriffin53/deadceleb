import wikipedia
import time

import tkinter as tk

class MainApp():
    def __init__(self, name):
        self.root = tk.Tk()
        self.root.geometry("1200x100")
        self.text = tk.StringVar()
        self.label = tk.Label(self.root, textvariable=self.text) # create label
        self.label.config(font=("Courier", 44)) # set font
        self.text.set(name + " has died. :(") # set text
        self.root.attributes('-topmost', True) # set on top mode
        self.root.update()
        self.label.pack()
        self.root.mainloop()

def isAlive(name):
    page = wikipedia.page(name, auto_suggest=False)
    lines = page.content.split("\n")
    first_sentence = lines[0].split(".") # get first sentence
    # if the first sentence got cut off because of a . in their name (e.g. 'Jr.'), take the second and third sentences just to be sure
    first_sentences = first_sentence[0]
    if len(first_sentence) >= 2: first_sentences += first_sentence[1]
    if len(first_sentence) >= 3: first_sentences += first_sentence[2]
    # if "is" appears but not "was", they're alive
    if first_sentences.find(" is ") != -1 and first_sentences.find(" was ") == -1:
        return True
    # if "was" appears but not "is", they're dead
    elif first_sentences.find(" is ") == -1 and first_sentences.find(" was ") != -1:
        return False
    else:
        # both or neither appear
        # if "is" is before "was", they're alive
        if first_sentences.find(" is ") < first_sentences.find(" was "):
            return True
        # otherwise, they're dead
        else:
            return False
    return True

sleep_delay = 300 # time to wait between checks
names = []
ff = open('celebs.txt', 'r')

for line in ff.readlines():
    names.append(line.replace('\n', ''))

while True:
    print("Checking " + str(len(names)) + " celebrities.")
    for name in names:
        alive = isAlive(name)
        alive_str = "Alive"
        if not alive:
            alive_str = "Dead"
        print(name, "-", alive_str)
        if not alive:
            app = MainApp(name)
    time.sleep(sleep_delay)
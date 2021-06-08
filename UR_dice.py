from tkinter import Tk, Label, Button, Entry
from random import *
import time

class Root(Tk):
    def __init__(self):
        super().__init__()
        
        self.title_label = Label(self, text="\n\nA simple dice simulator for tue game of UR:\n")
        self.title_label.pack()

        self.dice_label = Label(self, text="\n\nHow many dice?\n")
        self.dice_label.pack()

        self.entry = Entry(self)
        self.entry.pack()
        
        self.labelHidden = Label(self, text="\n\n\n")
        self.labelHidden.pack()
        
        self.button = Button(self, text="Roll the dice!", command=self.onclick)
        self.button.pack()
        
        self.labelHidden = Label(self, text="\n\n\n")
        self.labelHidden.pack()     
        
        self.label1 = Label(self, text="You rolled:\n\n")
        self.label1.pack()
        
        self.label = Label(self, font=("Arial", 55),  text="result")
        self.label.pack()
   
             
    def onclick(self):
        dice = int(self.entry.get())
        rounds = 0
        y = 0
        while rounds < dice:
        	x = randint(0, 1)
        	y = y+x
        	rounds = rounds + 1
        self.label.configure(text=str(y))            


root = Root()
root.mainloop()

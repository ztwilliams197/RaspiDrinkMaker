import tkinter as tk
from PIL import Image, ImageTk
import os

class Drink():

    def __init__(self, root, name, image, volume, liquid):
        self.button_frame = tk.Frame(master=root)
        self.name = tk.Label(master = self.button_frame, text=name)
        self.image = ImageTk.PhotoImage(Image.open(os.path.abspath(image)).resize((100,100), Image.ANTIALIAS))
        self.button = tk.Button(master = self.button_frame, image = self.image, command=lambda : self.dispense())
        self.volume = volume
        self.liquid = liquid
        self.name.grid(row=0,column=0)
        self.button.grid(row=1,column=0)
    
    def grid(self, row, column=0):
        self.button_frame.grid(row=row, column=column)
    
    def dispense(self):
        print(f"Dispensing {self.volume} of {self.liquid}")
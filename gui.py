import tkinter as tk
from drink import Drink

class GUI():

    def __init__(self, title, message):
        self.window = tk.Tk()
        self.window.title(title)
        tk.Label(text = message).pack(side = tk.TOP)
        self.drink_frame = tk.Frame()
        self.drinks = []
    
    def run(self):
        self.window.geometry("%dx%d" % (self.window.winfo_screenwidth(), self.window.winfo_screenheight()))
        self.drink_frame.pack()
        self.window.mainloop()
    
    def add_drink(self, drink_name, volume, liquid):
        self.drinks.append(Drink(self.drink_frame, drink_name, "DrinkImages\\" + drink_name + ".png", volume=volume, liquid=liquid))
        self.organize_drinks()
    
    def organize_drinks(self):
        for i in range(len(self.drinks)):
            self.drinks[i].grid(row=0, column=i)
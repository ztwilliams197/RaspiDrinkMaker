from gui import GUI

screen = GUI("Drink Maker", "Choose Your Drink")
screen.add_drink(drink_name="Vodka", volume=1.5, liquid="Vodka")
screen.add_drink(drink_name="Whiskey", volume=1.5, liquid="Whiskey")
screen.run()
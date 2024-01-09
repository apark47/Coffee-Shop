# DrinkOrder.py
from Coffee import Coffee
from FruitJuice import FruitJuice
from Beverage import Beverage

class DrinkOrder():
    def __init__(self):
        self.drinks = []
        
    def addBeverage(self, beverage):
        self.drinks.append(beverage)

    def getTotalOrder(self):
        total_price = 0.0
        receipt = "Order Items:\n"

        for i in self.drinks:
            total_price += i.getPrice()
            receipt += "* " + i.getInfo() + "\n"

        receipt += f"Total Price: ${total_price:.2f}"
        return receipt

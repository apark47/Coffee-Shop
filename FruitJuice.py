# FruitJuice.py
from Beverage import Beverage

class FruitJuice(Beverage):
    def __init__(self, ounces, price, fruits):
        super().__init__(ounces, price)
        self.fruits = fruits

    def getInfo(self):
        fruit_mix = ""
        basic_info = super().getInfo()

        for index, item in enumerate(self.fruits):
            
            if index <= len(self.fruits) - 2:
                fruit_mix += (item + "/")
            else:
                fruit_mix += item
            
                
        return f"{fruit_mix} Juice, {basic_info}"

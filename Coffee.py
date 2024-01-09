# Coffee.py
from Beverage import Beverage

class Coffee(Beverage):

    def __init__(self, ounces, price, style):
        super().__init__(ounces, price)
        self.style = style

    def getInfo(self):
        basic_info = super().getInfo()
        return f"{self.style} Coffee, {basic_info}"

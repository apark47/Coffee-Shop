# testFile.py

from Beverage import Beverage
from Coffee import Coffee
from FruitJuice import FruitJuice
from DrinkOrder import DrinkOrder


def test_BeverageConstructor():
    b = Beverage(90, 91.5)
    assert b.getOunces() == 90
    assert b.getPrice() == 91.5
    assert b.getInfo() == "90 oz, $91.50"

    b.updateOunces(10)
    b.updatePrice(5.0)
    assert b.getOunces() == 10
    assert b.getPrice() == 5.0

    a = Beverage(3, 10.0)
    assert a.getOunces() == 3
    assert a.getPrice() == 10.0
    assert a.getInfo() == "3 oz, $10.00"

    a.updateOunces(27)
    a.updatePrice(51.0)
    assert a.getOunces() == 27
    assert a.getPrice() == 51.0

    c = Beverage(9, 21.0)
    assert c.getOunces() == 9
    assert c.getPrice() == 21.0
    assert c.getInfo() == "9 oz, $21.00"

    c.updateOunces(65)
    c.updatePrice(5.5)
    assert c.getOunces() == 65
    assert c.getPrice() == 5.5
   

def test_FruitJuiceConstructor():
    j = FruitJuice(4, 5.0, ["Apple", "Banana"])
    assert j.getOunces() == 4
    assert j.getPrice() == 5.0
    assert j.getInfo() == "Apple/Banana Juice, 4 oz, $5.00"
    
    j.updateOunces(8)
    j.updatePrice(6.0)
    assert j.getOunces() == 8
    assert j.getPrice() == 6.0

    j2 = FruitJuice(9, 1.0, ["Banana"])
    assert j2.getInfo() == "Banana Juice, 9 oz, $1.00"

    j3 = FruitJuice(2, 4.0, ["Banana", "Apple", "Guava"])
    assert j3.getInfo() == "Banana/Apple/Guava Juice, 2 oz, $4.00"



def test_CoffeeConstructor():
    c = Coffee(1, 2.0, "Expresso")
    assert c.getOunces() == 1
    assert c.getPrice() == 2.0
    assert c.getInfo() == "Expresso Coffee, 1 oz, $2.00"

    c.updateOunces(3)
    c.updatePrice(4.0)
    assert c.getOunces() == 3
    assert c.getPrice() == 4.0
    assert c.getInfo() == "Expresso Coffee, 3 oz, $4.00"

    c2 = Coffee(8, 7.0, "Americano")
    assert c2.getOunces() == 8
    assert c2.getPrice() == 7.0
    assert c2.getInfo() == "Americano Coffee, 8 oz, $7.00"

    c3 = Coffee(9, 10.0, "Cappuccino")
    assert c3.getOunces() == 9
    assert c3.getPrice() == 10.0
    assert c3.getInfo() == "Cappuccino Coffee, 9 oz, $10.00"

    
def test_DrinkOrderConstructor():

    order = DrinkOrder()
    assert order.getTotalOrder() == "Order Items:\nTotal Price: $0.00"

    a = Coffee(8, 3.0, "Espresso")
    b = FruitJuice(16, 4.5, ["Apple", "Guava"])
    order = DrinkOrder()
    order.addBeverage(a)
    order.addBeverage(b)

    assert order.getTotalOrder() == "Order Items:\n\
* Espresso Coffee, 8 oz, $3.00\n\
* Apple/Guava Juice, 16 oz, $4.50\n\
Total Price: $7.50"
    
    c = Coffee(4, 5.0, "Cappuccino")
    d = Coffee(3, 4.0, "Americano")
    e = FruitJuice(14, 1.0, ["Orange", "Blueberry", "Guava"])
    f = FruitJuice(17, 5.0, ["Banana"])
    order = DrinkOrder()
    order.addBeverage(c)
    order.addBeverage(d)
    order.addBeverage(e)
    order.addBeverage(f)

    assert order.getTotalOrder() == "Order Items:\n\
* Cappuccino Coffee, 4 oz, $5.00\n\
* Americano Coffee, 3 oz, $4.00\n\
* Orange/Blueberry/Guava Juice, 14 oz, $1.00\n\
* Banana Juice, 17 oz, $5.00\n\
Total Price: $15.00"

    order2 = DrinkOrder()
    g = Coffee(12, 3.9, "Cappuccino")
    order2.addBeverage(g)
    assert order2.getTotalOrder() == "Order Items:\n\
* Cappuccino Coffee, 12 oz, $3.90\n\
Total Price: $3.90"

    order3 = DrinkOrder()
    h = FruitJuice(31, 9.409, ["Strawberry", "Orange"])
    order3.addBeverage(h)
    assert order3.getTotalOrder() == "Order Items:\n\
* Strawberry/Orange Juice, 31 oz, $9.41\n\
Total Price: $9.41"

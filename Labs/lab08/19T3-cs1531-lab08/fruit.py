# Author: @abara15 (GitHub)
price = 5.00

class order:
    def __init__(self):
        self.quantity = 0
        self.fruitType = ""
        self.orderID = 0
        self.status = ""
    def quantity(self):
        return self.quantity
    def fruitType(self):
        return self.fruitType
    def orderID(self):
        return self.orderID
    def status(self):
        return self.status

class fruit:
    def __init__(self):
        self.quantity = 0
        self.fruitType = ""
        self.price = 0
    def quantity(self):
        return self.quantity
    def fruitType(self):
        return self.fruitType
    def price(self):
        return price * self.price

class wholesaler:
    def __init__(self):
        self.numberOfOrders = 0
        self.allOrders = []
    def numberOfOrders(self):
        return self.numberOfOrders
    def allOrders(self):
        return self.allOrders

class customer:
    def __init__(self):
        self.name = ""
        self.orders = []
    def name(self):
        return self.name
    def orders(self):
        return self.orders




if __name__ == "__main__":

    customer.name = input("Enter name: ")
    fruitName = input("Enter fruit: ")
    if (fruitName is "Apple") or (fruitName is "Banana") or (fruitName is "Pear"):
        order.fruitType = fruitName
    else:
        raise ValueError("Invalid fruit name!")

    if order.quantity <= fruit.quantity:
        order.status = "fulfilled"
    else:
        order.status = "pending"
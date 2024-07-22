class Item():
    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

item1 = Item("Phone", 100, 20)

item2 = Item("card", 100)

print(item2.quantity)




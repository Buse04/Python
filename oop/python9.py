import csv 

class Item:
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        #run validation to recieved arguments
        assert price >= 0
        assert quantity >= 0

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)


    def __repr__(self):
        all= []
        return f"Item ('{self.name}', '{self.price}', '{self.quantity}')"
    
class Phone(Item):
    def __init__(self, name:str, price:float, quantity=0, broken_phones=0):
        super().__init__(name, price,quantity)
        self.broken_phones = broken_phones

    
    def total_quantity(self):
        return self.quantity - self.broken_phones

item1 = Phone("Phone", 100, 20, 5)

item2 = Item("card", 100)      
print(Item.all)

    
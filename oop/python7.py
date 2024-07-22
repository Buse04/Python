class Item():
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
        return f"Item ('{self.name}', '{self.price}', '{self.quantity}')"
    

item1 = Item("Phone", 100 , 5)

item2 = Item("Card", 200)

print(Item.all)
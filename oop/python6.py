class Item():
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        #run validation to recieved arguments
        assert price >= 0
        assert quantity >= 0

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self) # add all the items to list

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    

item1 = Item("Phone", 100 , 5)
item1.apply_discount()

item2 = Item("Card", 200)

print(item1.price)
print(item1.calculate_total_price()) #methodları parantez ile çağır aynı c# gibi
print(item2.calculate_total_price())

for instance in Item.all:
    print(instance.name) # rather than doing that we can use __repr__
    

class Item:
    def calculate_price(self, x, y):
        return x * y
    
item1 = Item()
item1.name = "phone"
item1.price = 4
item1.quantity = 5
print(item1.calculate_price(item1.price, item1.quantity))
    #item1 is here self in calculate_price method

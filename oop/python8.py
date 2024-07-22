import csv

class Item():

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            print(item)
    

    @staticmethod
    def get_integers(num):
        if isinstance(num, float):
            return num.get_integers()
        elif isinstance(num,int):
            return True
        else:
            return False
        
            
print(Item.get_integers(7))
Item.instantiate_from_csv()
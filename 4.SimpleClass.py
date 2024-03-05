import csv

class Item:
    pay_rate = 0.8 # class attribute
    all = []
    
    def __init__(self, name: str, price: float, quantity = 0):
        print("The object is initialized!")
        # run validations to received arguments
        assert price >= 0, f"Price {price} is not greater or equal to than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to than zero!"
                
        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        Item.all.append(self)
    
    def display(self): 
        print(self)
        print(self.name)
        print(self.quantity)
        print(self.price)
    
    def calculate(self, x, y): 
        return x * y
    
    @classmethod
    def instantiate_from_csv(cls): 
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items: 
            print(item) 
    
    def __repr__(self): 
        return f"Item('{self.name}', {self.quantity}, {self.price})"

# item1 = Item()
# item1.name = "Phone"
# item1.quantity = 2
# item1.price = 1200
# item1.display()
# print(item1.calculate(item1.quantity, item1.price))

# item2 = Item("Laptop", 2000, 3)

# print(Item.pay_rate)
# print(Item.__dict__) # all attribute for class level
# print(item2.__dict__) # all attribute for instance level

# item3 = Item("Watch", 200, 15)
# item3.pay_rate = 0.5
# print(item3.pay_rate)

# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 1)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

# print(Item.all)

Item.instantiate_from_csv()


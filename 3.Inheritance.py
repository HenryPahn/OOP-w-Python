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
    
    def calculate(self): 
        return self.quantity * self.price
    
    @classmethod
    def instantiate_from_csv(cls): 
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items: 
            print(item) 
    
    def __repr__(self): 
        return f"{self.__class__.__name__}('{self.name}', {self.quantity}, {self.price})"
    
class Phone(Item): 
    all = []
    def __init__(self, name: str, price: float, quantity = 0, broken_phone = 0): 
        # Call 'super()' function to have access to the parent's methods and attributes
        super().__init__(
            name, price, quantity
        )
        
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        assert broken_phone >= 0, f"Broken Phones {broken_phone} is not greater than or equal to zero!"
        
        self.broken_phone = broken_phone
        
        Phone.all.append(self)
        
phone1 = Phone("jscPhoenv10", 500, 5, 1)
print(phone1.calculate())
print(Item.all)
print(Phone.all)
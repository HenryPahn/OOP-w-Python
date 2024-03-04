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
        self.__name = name
        self.price = price
        self.quantity = quantity
        
        Item.all.append(self)
    
    @property
    def name(self): 
        return self.__name
    
    @name.setter 
    def name(self, value): 
        if(len(value) > 10):
            raise Exception("Name is too long")
        else:
            self.__name = value 
    
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
    
    def __printName(self): 
        print("fasdfasdf")
    
    def accessPrivMethod(self): 
        self.__printName()
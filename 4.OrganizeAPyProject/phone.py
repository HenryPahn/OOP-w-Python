from item import Item

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
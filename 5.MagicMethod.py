class Vector: 
    def __init__(self, x, y): 
        self.x = x
        self.y = y
        
    def __add__(self, other): 
        return Vector(self.x + other.x, self.y + other.y)
    
    def __call__(self): 
        print("I was called")
    
    def __repr__(self): 
        return f"{self.__class__.__name__}(x: {self.x}, y: {self.y})"
    
v1 = Vector(10, 20)
v2 = Vector(50, 60)
v3 = v1 + v2

v3()
print(v3)
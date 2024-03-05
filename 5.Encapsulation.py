class Person: 
    def __init__(self, name, age, gender): 
        assert len(name) > 0 and len(name) < 20, "The length of the name should be between 0 and 20"
        assert age > 0, "The age must be higher than 0"
        assert gender == "f" or gender == "m", "Invalid gender"
        
        self.__name = name 
        self.__age = age
        self.__gender = gender
        
    def __call__(self): 
        print(f"Say hello from {self.__name}")
    
    def __repr__(self): 
        return f"Hi, I am {self.__name}, {self.__age}, {self.__gender}"
    
    @property
    def Name(self): 
        return self.__name
    
    @Name.setter
    def Name(self, value): 
        if len(value) <= 0 or len(value) >= 20: 
            raise Exception("The length of the name should be between 0 and 20")
        else:
            self.__name = value
    
    @staticmethod
    def mymethod(): 
        print("Say hello from static method")
    
hoang = Person("Hoang", 21, "m")
hoang() # __call__ magic 
# hoang.Name = "dfklaks" # setter decorator
print(hoang) # __repr__ magic 
print(hoang.Name) # property decorator 
hoang.mymethod() # staticmethod decorator

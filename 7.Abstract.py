# NOTE: this example code is not really the way implement an abstract class 

from abc import ABCMeta, abstractstaticmethod

class Person(metaclass = ABCMeta):     
    @abstractstaticmethod
    def person_method(): 
        # This is pure virtual function in cpp. Only have declaration, no definition. 
        pass

class Student: 
    def __init__(self): 
        self.name = "Basic student Name"
        
    def person_method(self): 
        print("I am a student")
        
class Teacher: 
    def __init__(self): 
        self.name = "Basic teacher name"
        
    def person_method(self): 
        print("I am a teacher")

def build_person(person_type):
    PERSONTYPES = {"Student":Student, "Teacher":Teacher} # dictionary. The same as JSON object in js 
    return PERSONTYPES[person_type]()

# s1 = Student()
# s1.person_method()

# t1 = Teacher()
# t1.person_method()

if __name__ == "__main__": 
    choice = input("What type of person?\n")
    person = build_person(choice)
    person.person_method()
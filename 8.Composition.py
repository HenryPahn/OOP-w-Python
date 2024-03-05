from abc import ABCMeta, abstractmethod, abstractstaticmethod

class Department(metaclass = ABCMeta): 
    @abstractmethod
    def __init__(self, employees): 
        pass
    @abstractmethod
    def print_department(): 
        pass
    
class Accounting(Department): 
    def __init__(self, employees): 
        self.employees = employees
        
    def print_department(self):
        print(f"Accouting department: {self.employees}")
        
class Development(Department): 
    def __init__(self, employees): 
        self.employees = employees
        
    def print_department(self): 
        print(f"Development Department: {self.employees}")
        
class ParentDepartment(Department): 
    def __init__(self, employees): 
        self.employees = employees 
        self.base_employees = employees
        self.sub_depts = []
        
    def add(self, dept): 
        self.sub_depts.append(dept)
        self.employees += dept.employees
        
    def print_department(self): 
        print(ParentDepartment)
        print(f"Parent Department Base employees: {self.base_employees}")
        for dept in self.sub_depts:
            dept.print_department()
        print(f"Total number of employees: {self.employees}")
        
dept1 = Accounting(200)
dept2 = Development(170)

parent_dept = ParentDepartment(30)
parent_dept.add(dept1)
parent_dept.add(dept2)

parent_dept.print_department()


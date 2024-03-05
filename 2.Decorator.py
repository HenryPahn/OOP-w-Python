import time

# #Step 1: Define the decorator function
# def decorator_name(target_function):

#         #Step 2: Define the wrapper function
#     def wrapper(*args, **kwargs):

#         #Step 3: Do something before target_function is called
#         results = target_function( * args, ** kwargs)

#         # Step 4: Do something after the call to target_function
#         return results
#     return wrapper # Step 5: return wrapper function 

# def mydecorator(function):
#     def wrapper(): 
#         function()
#         print("I am decorating your function!")
#     return wrapper

# def basic_decorator(): 
#     print("Hello world")

# mydecorator(basic_decorator)()

# @mydecorator
# def common_decorator(): 
#     print("Hello my world")

# common_decorator()

def timed(function): 
    def wrapper(*args, **kwargs): 
        before = time.time()
        function(*args, ** kwargs)
        after = time.time()
        print(f"{function.__name__} tool {after - before} seconds to execute!")
    return wrapper

@timed
def myfunction(x): 
    result = 1 
    for i in range(1, x): 
        result += i
    
myfunction(1000000)
    
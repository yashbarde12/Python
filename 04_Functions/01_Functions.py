# Functions in python
'''
- Functions are blocks of reusable code designed to perform a specific task.
- They enhance code readability, reusability, and modularity.
- It is executed when it is called 
- Two Types of Functions in python:
    1. Built in function    : Predefined functions in python.
        Example : type(), input(), eval()...etc
    2. User Defined Function: Defined by user to perform a task.
        Syntax : 
            def function_name(parameters):          #function def
                                statement1
                                stetement2
                                return expression
            function_name(arguments)                #function call 
- Parameters: Variables listed in a function's definition.
- Arguments: Values passed into a function when it is called.
- return : Ends the function's execution and optionally returns a value to the caller.
- If no return statement is specified, the function returns None by default.
'''
#--------------------------------------------------------
# Function without parameters
print("----- Function without parameters -----")
def add():     #add is a function name
   x = 10
   y = 20
   result = x + y
   print(result) # 30

add() # 30     #function call       
add() # 30     # We can call function as many times we want

#--------------------------------------------------------
# Function with parameters
print("----- Function with parameters -----")
def sub(x,y):   # x and y are parameters : value required for the funcion.
   result1 = x - y
   print(result1) 
   p = x
   q = y
   result2 = q - p
   print(result2)

sub(30,20)     # 30, 20 are arguments : value passed to the function.
'''  10
    -10  '''

sub(40,20)     # 40, 20 are arguments : value passed to the function.
'''  20
    -20  '''   

# sub(50)      # TypeError: sub() missing 1 required positional argument: 'y'

#--------------------------------------------------------
# Call by Value
print("----- Call by Value -----")
'''
- if we pass an immutable object (e.g., numbers, strings, tuples) to a function,
- value of the object cannot be changed within the function.
- Function receives a copy of the value,
- any modifications made to the parameter inside the function do not affect the original object.
'''
def modify_value(x):
    x = x + 1
    print("Inside function:", x)

num = 10
modify_value(num) # Inside function: 11
print("Outside function:", num) # Outside function: 10

#--------------------------------------------------------
# Call by Reference
print("----- Call by Reference -----")
'''
- if we pass a mutable object (e.g., lists, dictionaries) to a function, 
- it behaves more like "call by reference" because the function can modify the object in-place.
- The reference to the object is passed to the function,
- any changes made to the object inside the function affect the original object.
'''
def modify_list(lst):
    lst.append(4)
    print("Inside function:", lst)

my_list = [1, 2, 3]
modify_list(my_list) # Inside function: [1, 2, 3, 4]
print("Outside function:", my_list) # Outside function: [1, 2, 3, 4]

#--------------------------------------------------------
#--------------------------------------------------------

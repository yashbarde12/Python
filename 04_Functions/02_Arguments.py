# Arguments
'''
- Arguments: Values passed into a function when it is called.
- Types of arguments:
        1. Positional/Required Arguments
        2. Default Arguments
        3. Keyword arguments
        4. Variable Length Arguments
'''
#--------------------------------------------------------
# Positional/Required Arguments
print("----- Positional/Required Arguments -----")
'''
- Required arguments are to be passed at the time of function call with the exact match of their positions.
- If either of the arguments is not provided in the function call, or the position of the arguments is changed, 
- The Python interpreter will show the error.
- i.e number of arguments and position of arguments must be match. '''
def add(c,d):
    return c + d

a = 10
b = 20
print("Addition is:", add(a,b)) # Addition is: 30

# Uncomment one by one and run the cases
"""
# Case 1:
def add(c,d):
    return c + d

a = 10
b = 20
sum1 = add(a) # TypeError: add() missing 1 required positional argument: 'd'
print("Addition is:", sum1)
"""
"""
# Case 2:
def add(c):
    return c + d

a = 10
b = 20
sum1 = add(a,b) # TypeError: add() takes 1 positional argument but 2 were given
print("Addition is:", sum1)
"""
#--------------------------------------------------------
# Default Arguments
print("----- Default Arguments -----")
''' 
- If the value of any of the arguments is not provided at the time of function call
- Then that argument can be initialized with the default value given in the definition  
- But if the value is provided at the time of function call, 
  that value will be considered instead of default value.     '''
def add(c,d = 30): # Here d id default argument
    return c + d

a = 10
sum = add(a)
print("Addition is:", sum) # Addition is: 40

a = 10
b = 20
sum = add(a, b)
print("Addition is:", sum) # Addition is: 30

sum = add(b, a)
print("Addition is:", sum) # Addition is: 30

# Once default argument set, all next arguments must be default argument.
'''
def add(c, d = 30, e): # SyntaxError: non-default argument follows default argument
    return c + d + e  
a = 10
b = 20
sum = add(a, b, c)
print("Addition is:", sum)
'''
#--------------------------------------------------------
# Keyword Arguments
print("----- Keyword Arguments -----")
# We can pass argument value by keyword i.e by parameter name.
def greeting(name, msg):
    return "Hello! "+ name + msg

a = greeting(name = "Jim, ", msg = "Good day :)")
print(a) # Hello! Jim, Good day :)
b = greeting(msg = "Good day :)", name = "Jim, ")
print(b) # Hello! Jim, Good day :)
'''
- We can use both positional and keyword argument simultaneously.
- but first we have to take positional argument then keyword argument.
- i.e Positional argument cannot appear after keyword arguments. '''
def greeting(name, msg):
    return "Hello! "+ name + msg

a = greeting("Jim, ", "Good day :)") 
print(a) # Hello! Jim, Good day :)
a = greeting("Jim, ", msg = "Good day :)") 
print(a) # Hello! Jim, Good day :)
# a = greeting(name = "Jim", "Good day :)") #invalid
# print(a) # SyntaxError: positional argument follows keyword argument.
#--------------------------------------------------------
# Variable Length Arguments
print("----- Variable Length Arguments -----")
'''
- Only one paramter to multiple arguments.
- In the function call any number of values can be passed,
  which are treated as tuple in function definition.
- variable length argument is defined as 
        syntax: def function(*Variable_name):
'''
def fun(*n): # Here, n will be converted into tuple
    print("Type of passed argument:", type(n)) # Type of passed argument: <class 'tuple'>
    print("Printing the passed argumnets") # Printing the passed argumnets
    print(n) # ('Jim', 'Pam', 'Ash')

    for i in n:
        print(i)
        '''   Jim
              Pam
              Ash   '''

fun("Jim", "Pam", "Ash")
#--------------------------------------------------------
# Mixing all Arguments
print("----- Mixing all Arguments -----")
'''
A function with a mix of different types of arguments.
Parameters:
    - arg1: Positional argument
    - arg2: Positional argument
    - args: Variable positional arguments (collected into a tuple)
    - kwarg1: Default keyword argument
    - kwarg2: Default keyword argument
'''
# function defination
def mixing(arg1, arg2, *args, kwarg1="default_value1", kwarg2="default_value2"):
    
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("args:", args)
    print("kwarg1:", kwarg1)
    print("kwarg2:", kwarg2)
    
# function call
mixing("positional1", "positional2", "extra_arg1", "extra_arg2", kwarg2="custom_value")
''' Output:
            arg1: positional1
            arg2: positional2
            args: ('extra_arg1', 'extra_arg2')
            kwarg1: default_value1
            kwarg2: custom_value    '''
#--------------------------------------------------------
#--------------------------------------------------------

# Typer casting
'''
- Type casting : converting one data type into another.

- Types:
    1. Implicit type casting: automatic type casting.

    2. Explicit type casting: manual type casting with built in functions.
        - Primitive type casting
        - Derived or colletion data type casting
'''
#--------------------------------------------------------
# Implicit type casting
print("-----Implicit type casting-----")
x = 10 # Integer 
y = 3.14 # Float
result = x + y # Implicit conversion of integer to float 
print(result) # Output will be a float: 13.14 
print(type(result)) # 

#--------------------------------------------------------
# Explicit type casting
print("-----Explicit type casting-----")
'''
- Primitive type casting: 
    1. Integer  - int(a)
    2. Float    - float(b)
    3. Complex  - complex(a,b)
    4. String   - str(a)
    5. Boolean  - bool(a)

- Derived or colletion data type casting:
    1. List           - list()   
    2. Tuple          - tuple()
    3. Set            - set()
    4. Frozenset      - frozenset()
    5. Dictionary     - dict()
'''
#--------------------------------------------------------
print("-----Integer-----")
a = 3.142
b = int(a)
print(b) # 3

#--------------------------------------------------------
print("-----Float-----")
a = 10
b = float(a)
print(b) # 10.0

#--------------------------------------------------------
print("-----Complex-----")
p = 2
c = complex(p) #a+bj 
print(c) # (2+0j)
# Here a and b are two numbers(can be int or float)
# since we are passing only one argument, it becomes zero.

a = 10
b = 10.0
d = complex(a,b)
print(d) # (10+10j)

e = complex(50,26.3)
print(e) # (50+26.3j)

#--------------------------------------------------------
print("-----String-----")
a = 3.142
f = str(a)
print(f) # 3.142
print(type(f)) # <class 'str'>

#--------------------------------------------------------
print("-----Boolean-----")
a = 3.142
g = bool(a)
print(g) # True
#for bool, non zero numbers and non empty strings are true, all others false
print(bool(35)) # True
print(bool(-12)) # True
print(bool(0)) # False
print(bool(0.0)) # False
print(bool("hi")) # True
print(bool(" ")) # True
print(bool("")) # False

#--------------------------------------------------------
print("-----List-----")
a = 10, 20, 30, 20
print(type(a)) # <class 'tuple'>
list = list(a)
print(list) # [10, 20, 30, 20]
print(type(list)) # <class 'list'>

#--------------------------------------------------------
print("-----Tuple-----")
list = [10,20,30,20]
tuple = tuple(list)
print(tuple) # (10, 20, 30, 20)
print(type(tuple)) # <class 'tuple'>

#--------------------------------------------------------
print("-----Set-----")
list = [10,20,30,20]
set = set(list)
print(set) # {10, 20, 30}
print(type(set)) # <class 'set'>

#--------------------------------------------------------
print("-----Frozenset-----")
list = [10,20,30,20]
frozenset = frozenset(list)
print(frozenset) # frozenset({10, 20, 30})
print(type(frozenset)) # <class 'frozenset'>

#--------------------------------------------------------
#--------------------------------------------------------



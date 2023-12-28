# Tuples
'''
- Tuple is a ordered collection of different values or different types of items.
- Tuples are immutable means unchangable.
- Hetrogeneous: like lists, tuples is capable of storing different types of values.
- Items in list seperated by (,) ans enclosed in ().
- Duplicates are allowded in tuples.
'''
#--------------------------------------------------------
# Differences between lists and tuples
print("----- Differences between lists and tuples -----")

# Difference 1 : [] and ()
a = [1, 2, 3, 'Jim', 'Pam']
print(type(a)) # <class 'list'> 
b = (1, 2, 3, 'Jim', 'Pam')
print(type(b)) # <class 'tuple'>

# Difference 2 : Immutable
a = [1, 2, 3, 'Jim', 'Pam']
a[2] = 10
print(a) # [1, 2, 10, 'Jim', 'Pam']
b = (1, 2, 3, 'Jim', 'Pam')
#b[2] = 10
#print(b) # Error

# Difference 3 : Memory space
# list occupies more memory space as compared to tuple.
import sys
a = [1, 2, 'Jim', 'Pam', True, 'Angela']
b = (1, 2, 'Jim', 'Pam', True, 'Angela')
print("Size of list : ", sys.getsizeof(a)) # 152
print("Size of tuple : ", sys.getsizeof(b)) # 88

# Difference 4 : Memory space
# list takes more time to execute as compared to tuple.
import timeit
listtime = timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9]", number = 1000000)
tupletime = timeit.timeit(stmt="(1,2,3,4,5,6,7,8,9)", number = 1000000)
print("List takes time : ", listtime) # 0.3231110000051558
print("Tuple takes time : ", tupletime) # 0.030833799857646227
#--------------------------------------------------------
# Creating tuple
print("----- Creating tuple -----")
# Empty tuple
a = ()
print(a) # ()
print(type(a)) # <class 'tuple'>

# Tuple with only one element
# a = (12.23) # This is not tuple. if we check type then we Will get float.
# print(type(a)) # <class 'float'>
a = (12.23,)
print(a) # (12.23,)
print(type(a)) # <class 'tuple'>

# if we know emelents
a = (10,20,30)
print(a) # (10, 20, 30)
print(type(a)) # <class 'tuple'>

a = 100,200,300
print(a) # (100, 200, 300)
print(type(a)) # <class 'tuple'>

# Form string to tuple using tuple(variable) function
str = "hello"
a = tuple(str)
print(a) # ('h', 'e', 'l', 'l', 'o')
print(type(a)) # <class 'tuple'>

# Form list to tuple using tuple(variable) function
z = [11,22,33]
print(z) # [11, 22, 33]
a = tuple(z)
print(a) # (11, 22, 33)
print(type(a)) # <class 'tuple'>

# Form range() to tuple()
a = tuple(range(1,6))
print(a) # (1, 2, 3, 4, 5)
print(type(a)) # <class 'tuple'>
#--------------------------------------------------------
# Tuple Operators
print("----- Tuple Operators -----")
'''
1. Concatenation Operator : +
2. Replication Operator   : *
3. Membership Operators   : (in / not in)
4. Comparison Operators   : (<,>,<=,>=,==,!=)
'''
a = (1, 2)
b = (1, "Hello", 2, 1.1)

print(a + b) # (1, 2, 1, 'Hello', 2, 1.1)
print(a * 3) # (1, 2, 1, 2, 1, 2)

print(1.1 in b) # True
print(1.1 not in b) # False

print(a == a) # True
print(a != b) # True
#--------------------------------------------------------
# Accessing tuple values
print("-----Accessing tuple values-----")
x = (44,55,66,77,88,99)
print(x[0]) # 44
print(x[-1]) # 99
# print(x[12]) # Error # tuple index out of range
#--------------------------------------------------------
# Tuple Slicing
print("----- Tuple Slicing -----")
'''
- Same as string we have concept of tuple slicing in python.
- Slicing : selecting values in tuple between n and m
            starting at n, n+1, n+2,...till m-1
- Syntax :  Variable_name [start : end : step_value]
'''
a = ("Jim", 10, "Pam", 12.5)
print(a[0:]) # ('Jim', 10, 'Pam', 12.5)
print(a[1:3]) # (10, 'Pam')
'''
step 1 : Check sign of step value
step 2 : if Positive then indexing if forward, start from 0 
         if Negative then indexing if backward, start from -1 
step 3 : if step value is 2 then skip 1 character 
         i.e no of skip characters = step value -1
'''
a = (11, 22, "jim", 1.1, "I", 0)
print(a[-5:6:2]) # (22, 1.1, 0)
print(a[6:1:-1]) # (0, 'I', 1.1, 'jim')
#--------------------------------------------------------
# Operations on tuples
print("-----Operations on tuples-----")
"""
#--------------------------------------------------------
# Updating tuples
a = ("Jim", 10, "Pam", 12.5)
# print(a[1]) # 10
# a[1] = "Micheal"
# print(a[1]) # Error
#--------------------------------------------------------
# Deleting tuples
a = ("Jim", 10, "Pam", 12.5)
print(a) # ('Jim', 10, 'Pam', 12.5)
# del a[1] 
# print(a) # Error
a = ("Jim", 10, "Pam", 12.5)
del a
# print(a) # Error because whole tuple can be deleted.
#--------------------------------------------------------
a = ('Jim', 'Pam', 'Dwight', "Angela")
# a.append("Micheal")
# print(a) # Error

a = ()
for i in range(3):
    x = int(input("Enter number to add in tuple: "))
    # a.append(x) # Error
# print(a) 
#--------------------------------------------------------
""" 
'''
- Tuples are immutable so we can't perform different operations on tuples. 
- but there is another way to achieve this:
        - Step 1 : Convert tuple to list.
        - Step 2 : Perform operation on list.
        - Step 3 : Convert list back to tuple.
'''
a = ("Jim", 50, "Pam", 40)
b = list(a)
b[1] = "Angela"
print(b) # ['Jim', 'Angela', 'Pam', 40]
a = tuple(b)
print(a) # ('Jim', 'Angela', 'Pam', 40)
#--------------------------------------------------------
# len() 
print("-----len()-----")
''' This function used to find length of tuple. '''
a = ("Jim", 10, "Pam", 12.5)
print(len(a)) # 4
#--------------------------------------------------------
# tuple.count() 
print("-----tuple.count()-----")
# This function is used to count the frequency of objects in tuple
a = ('Jim', 'Pam', 'Jim', "Angela")
x = a.count("Jim")
print(x) # 2
#--------------------------------------------------------
# tuple.index() 
print("-----tuple.index()-----")
'''
- This function is used to find index of object/element in tuple.
- This function returns first index of object if object occurs multiple times in list.
'''
a = ('Jim', 'Pam', 'Jim', "Angela")
x = a.index("Jim")
# y = a.index("Ash")
print(x) # 0
# print(y) # ValueError: 'Ash' is not in tuple
#--------------------------------------------------------
# max() 
print("-----max()-----")
''' This function used to find maximum value in tuple. '''
a = [10, 20, 30, 40, 50]
print(max(a)) # 50
a = (10, "Jim") # comparison between string and int value
#print(max(a)) # TypeError: '>' not supported between instances of 'str' and 'int'
#--------------------------------------------------------
# min() 
print("-----min()-----")
''' This function used to find minimum value in tuple. '''
a = (10, 20, 30, 40, 50)
print(min(a)) # 10
a = ('ABC', 'abc', 'A') # comparison between string values
print(min(a)) # A # ASCII value will be compaired. # A:65 a:97
#--------------------------------------------------------
# sorted() 
print("-----sorted(tuple)-----")
# This function return a new list containing all items from the iterable in ascending order.
a = (5, 2, 8, 3, 7)
sorted(a)
print(a) # (5, 2, 8, 3, 7)
b = sorted(a)
print(b) # [2, 3, 5, 7, 8] # New list
#--------------------------------------------------------
# tuple()
print("-----tuple()-----")
'''
- This method is used as constructor.
- Which is used to create tuple from different types of values.
'''
# Form string
str = "hello"
a = tuple(str)
print(a) # ('h', 'e', 'l', 'l', 'o')
print(type(a)) # <class 'tuple'>

# Form list 
list = [11,22,33]
a = tuple(list)
print(a) # (11, 22, 33)
print(type(a)) # <class 'tuple'>

# From dictionary
dict = {1: "Jim", 2: "Pam"}
a = tuple(dict)
print(a) # (1, 2)
print(type(a)) # <class 'tuple'>

# Form range() to tuple()
a = tuple(range(1,6))
print(a) # (1, 2, 3, 4, 5)
print(type(a)) # <class 'tuple'>
#--------------------------------------------------------
# Packing and unpacking of tuple
print("-----Packing and unpacking of tuple-----")
# Packing : we can create tuple by packing group of variables.
a = 10
b = 20
c = 30
d = 40
t = a, b, c, d
print(t) # (10, 20, 30, 40)
print(type(t)) # <class 'tuple'>

# Unpacking : this is reverse process of packing tuples.
t = (10, 20, 30, 40)
a, b, c, d = t
print('a:',a, 'b:',b, 'c:',c, 'd:',d) # a: 10 b: 20 c: 30 d: 40

''' Note: while Packing & Unpcaking, values and varibales count must match'''
#--------------------------------------------------------
# Tuple Comprehensions
print("-----Tuple Comprehensions-----")
print("Tuple Comprehension is not suppoted by python.")
#--------------------------------------------------------
#--------------------------------------------------------
# Lists
'''
- List is a ordered collection of different values or different types of items.
- Hetrogeneous: Unlike array in C, C++, java a list is capable of storing different types of values.
- Items in list seperated by (,) ans enclosed in [].
- Lists provides facility to store multiple types of values in  single unit.
- Lists are mutable.
- Duplicates are allowded in lists.
- Indexing is present in lists.
'''
#--------------------------------------------------------
a = ["Jim", 1, "Pam", 12.5]
b = [1, 2, 3, 4, 5]
print("type of a: ",type(a)) # type of a:  <class 'list'>
print("type of b: ",type(b)) # type of b:  <class 'list'>
print(a[0]) # Jim
print(b[-1]) # 5
#--------------------------------------------------------
print("-----How to crerate a list-----")
# Empty list
list1 = []
print(list1) # []

# if we know emelents
list2 = [10,20,30]
print(list2) # [10, 20, 30]

# Form string to list using list(variable) function
str = "hello"
list3 = list(str)
print(list3) # ['h', 'e', 'l', 'l', 'o']

# Form string to list using split() function
a = "9-11-2023"
list4 = a.split("-")
print(list4) # ['9', '11', '2023']

# From range() function
list5 = list(range(1,6))
print(list5) # [1, 2, 3, 4, 5]
#--------------------------------------------------------
# List Operators
print("----- List Operators -----")
'''
1. Concatenation Operator : +
2. Replication Operator   : *
3. Membership Operators   : (in / not in)
4. Comparison Operators   : (<,>,<=,>=,==,!=)
'''
a = [1, 2]
b = [1, "Hello", 2, 1.1]

print(a + b) # [1, 2, 1, 'Hello', 2, 1.1]
print(a * 3) # [1, 2, 1, 2, 1, 2]

print(1.1 in b) # True
print(1.1 not in b) # False

print(a == a) # True
print(a != b) # True
#--------------------------------------------------------
# Accessing list values
print("-----Accessing list values-----")
x = [44,55,66,77,88,99]
print(x[0]) # 44
print(x[-1]) # 99
#print(x[12]) # Error # list index out of range
#--------------------------------------------------------
# List Slicing
print("----- List Slicing -----")
'''
- Same as string we have concept of list slicing in python.
- Slicing : selecting values in list between n and m
            starting at n, n+1, n+2,...till m-1
- Syntax :  Variable_name [start : end : step_value]
'''
a = ["Jim", 10, "Pam", 12.5]
print(a[0:]) # ['Jim', 10, 'Pam', 12.5]
print(a[1:3]) # [10, 'Pam']
'''
step 1 : Check sign of step value
step 2 : if Positive then indexing if forward, start from 0 
         if Negative then indexing if backward, start from -1 
step 3 : if step value is 2 then skip 1 character 
         i.e no of skip characters = step value -1
'''
a = [11, 22, "jim", 1.1, "I", 0]
print(a[-5:6:2]) # [22, 1.1, 0]
print(a[6:1:-1]) # [0, 'I', 1.1, 'jim']
#--------------------------------------------------------
# Operations on list
'''
- Since lists are mutable we can perform different operations on lists.
- Updating
- Deleting
- Inserting
- Adding
'''
#--------------------------------------------------------
# Updating list
print("----- Updating list -----")
a = ["Jim", 10, "Pam", 12.5]
print(a[1]) # 10
a[1] = "Micheal"
print(a[1]) # Micheal
print(a) # ['Jim', 'Micheal', 'Pam', 12.5] 
''' '10' update to 'Micheal' and '10' is removed '''
#--------------------------------------------------------
# Deleting list
print("----- Deleting list -----")
a = ["Jim", 10, "Pam", 12.5]
print(a) # ['Jim', 10, 'Pam', 12.5]
del a[1] 
print(a) # ['Jim', 'Pam', 12.5]
del a
# print(a) # Error because list is deleted
#--------------------------------------------------------
# List functions
print("----- List functions -----")
#--------------------------------------------------------
# len() 
print("-----len()-----")
''' This function used to find length of list. '''
a = ["Jim", 10, "Pam", 12.5]
print(len(a)) # 4
#--------------------------------------------------------
# list.count() 
print("-----list.count()-----")
# This function is used to count the frequency of objects in list
a = ['Jim', 'Pam', 'Jim', "Angela"]
x = a.count("Jim")
print(x) # 2
#--------------------------------------------------------
# list.index() 
print("-----list.index()-----")
'''
- This function is used to find index of object/element in list.
- This function returns first index of object if object occurs multiple times in list.
'''
a = ['Jim', 'Pam', 'Jim', "Angela"]
x = a.index("Jim")
# y = a.index("Ash")
print(x) # 0
# print(y) # ValueError: 'Ash' is not in list
#--------------------------------------------------------
# max() 
print("-----max()-----")
''' This function used to find maximum value in list. '''
a = [10, 20, 30, 40, 50]
print(max(a)) # 50
a = [10, "Jim"] # comparison between string and int value
#print(max(a)) # TypeError: '>' not supported between instances of 'str' and 'int'
#--------------------------------------------------------
# min() 
print("-----min()-----")
''' This function used to find minimum value in list. '''
a = [10, 20, 30, 40, 50]
print(min(a)) # 10
a = ['ABC', 'abc', 'A'] # comparison between string values
print(min(a)) # A # ASCII value will be compaired. # A:65 a:97
#--------------------------------------------------------
# list.append() 
print("-----list.append()-----")
'''
- This function is used to append (add) a passed object at end of list.
- object is added to last of list hence indexing is changed.
'''
a = ['Jim', 'Pam', 'Dwight', "Angela"]
a.append("Micheal")
print(a) # ['Jim', 'Pam', 'Dwight', 'Angela', 'Micheal'] 

a = []
for i in range(3):
    x = int(input("Enter number to add in list: "))
    a.append(x)
print(a) # [11, 22, 33]
#--------------------------------------------------------
# list.extend() 
print("-----list.extend()-----")
'''
- To add all items of one list to another list.
- Syntax: list1.extend(list2)
- i.e all items present in list2 will be added to list1
'''
a = ['Jim', 'Micheal', 'Dwight']
b = [11, 12, 13]
a.extend(b)
print(a) # ['Jim', 'Micheal', 'Dwight', 11, 12, 13]

a = ['Jim', 'Micheal', 'Dwight']
a.extend("Pam") # Passing a string instead of another list
print(a) # ['Jim', 'Micheal', 'Dwight', 'P', 'a', 'm'] 
#--------------------------------------------------------
# list.insert()
print("-----list.insert()-----")
'''
- This function is used to insert the value at given index in list.
- Syntax: list.insert(index, value)
'''
a = [5, "jim", 10]
a.insert(2, "Pam")
print(a) # [5, 'jim', 'Pam', 10]
a.insert(15, "Ash")
print(a) # [5, 'jim', 'Pam', 10, 'Ash']
#--------------------------------------------------------
# list.remove() 
print("-----list.remove()-----")
'''
- This function is used to remove the value from given list.
- This function removes first occurrence of object if object occurs multiple times in list.
- Syntax: list.remove(value)
'''
a = [5, 'jim', 'Pam', 10, 'Ash', 'Pam']
a.remove('Pam')
print(a) # [5, 'jim', 10, 'Ash', 'Pam']
#--------------------------------------------------------
# list.pop() 
print("-----list.pop(inedex)-----")
'''
- Remove and return item at index (default last).
- This function removes the last value of list of index not given.
- Syntax: list.pop()
'''
a = [5, 2, 8, 3, 7]
a.pop() # 7 removed
print(a.pop()) # 3
print(a) # [5, 2, 8]
print(a.pop(0)) # 5
print(a) # [2, 8]
#--------------------------------------------------------
# list.reverse() 
print("-----list.reverse()-----")
'''
- This function is used to reverse the values present in the list in place.
- Here the word in place means that list get reversed itself.
- Syntax: list.remove(value)
'''
a = [5, 'jim', 'Pam', 10, 'Ash', 'Pam']
a.reverse()
print(a) # ['Pam', 'Ash', 10, 'Pam', 'jim', 5]
a = [1, 2, 3]
b = a.reverse() 
print(b) # None 
''' 
- it gives None.
- we can,t access the it to another variable.
- a.reverse() is it's own reveresd list itself.
'''
#--------------------------------------------------------
# list.sort() 
print("-----list.sort()-----")
'''
- This function is used to sort the values present in the list in either acending or descending order.
- The list is sorted itself.
- Note: sorting is done with similar datatypes only,  otherwise it gives error.
- By default sorting is done in acending order.
- Syntax: list.sort(reverse=False)
          list.sort(reverse=True)
'''
a = [5, 2, 8, 3, 7]
a.sort()
print(a) # [2, 3, 5, 7, 8]
a.sort(reverse=True)
print(a) # [8, 7, 5, 3, 2]

b = a.sort()
print(b) # None 
''' 
- it gives None.
- we can,t access the it to another variable.
- a.sort() is it's own sorted list itself.
'''
#--------------------------------------------------------
# list.copy() 
print("-----list.copy()-----")
# Return a shallow copy of the list.
a = [5, 2, 8, 3, 7]
b = a.copy()
print(b) # [5, 2, 8, 3, 7]
#--------------------------------------------------------
# list.clear() 
print("-----list.clear()-----")
# This function remove all elements in list.
a = [5, 2, 8, 3, 7]
print(a) # [5, 2, 8, 3, 7]
a.clear()
print(a) # []
#--------------------------------------------------------
# Nested Lists
print("-----Nested Lists-----")
# We can take one or multiple list(s) inside another list.
a = [10, 20, [30, 40]]
print(a[0]) # 10
print(a[2]) # [30, 40]
print(a[2][0]) # 30
print(a[2][1]) # 40
#--------------------------------------------------------
# List Comprehensions
print("-----List Comprehensions-----")
'''
- It is easy and compact way of creating list objects from any iterable objects.
- Syntax: list = [expression  for item in list  if condition]
'''
list = [1, 2, 3, 4, 5]
a = [x*x  for x in list]
print(a) # [1, 4, 9, 16, 25]

b = [x**3 for x in list]
print(b) # [1, 8, 27, 64, 125]

c = [x for x in list if x % 2 == 0]
print(c) # [2, 4]
#--------------------------------------------------------
print("-----Without comprehension-----")
a = ['Jim', 'Pam', 'Ash', 'Pam']
b = []
for i in a:
    b.append(i[0])
print(b) # ['J', 'P', 'A', 'P']


print("-----With comprehension-----")
a = ['Jim', 'Pam', 'Ash', 'Pam']
b = [i[0] for i in a ]
print(b) # ['J', 'P', 'A', 'P']
#--------------------------------------------------------
#--------------------------------------------------------



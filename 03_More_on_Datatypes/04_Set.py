# Set
'''
- Set is a unordered collection of different values or different types of items.
- Set contain only unique elements, duplicates are automatically removed.
- Hetrogeneous: like lists and tuples, set is capable of storing different types of values.
- Mutable (for the elements): but the set itself (as a whole) is immutable.
- Items in list seperated by (,) ans enclosed in {}.
- We can apply mathematical operations like union, intersection, difference etc on objects.
- Insertion order is not preserved, but we can sort elements
- Indexing and sclicing are not allowded in sets.
'''
#--------------------------------------------------------
# Creating set
print("----- Creating set -----")

# If we know elements
s = {10, 20, 30, 40}
print(s) # {40, 10, 20, 30}
print(type(s)) # <class 'set'>   

# Using set() function
a = [10, 20, 30, 40, 10, 20, 10]
b = set(a)
print(b) # {40, 10, 20, 30}
print(type(b)) # <class 'set'>  

# Using range() function
s = set(range(5))
print(s) # {0, 1, 2, 3, 4}

# Creating empty set
'''
- While creating empty set we have to take special care.
- compulsory we must use set() function.
- a = {} is treated as dictionary not empty set.
'''
s = set()
print(s) # set() # Empty set
print(type(s)) # <class 'set'>

a = {}
print(a) # {}
print(type(a)) # <class 'dict'>
#--------------------------------------------------------
# Set Functions
print("----- Set Functions -----")
#--------------------------------------------------------
# set.add()
print("----- set.add(x) -----")
'''
- Add single item to set.
- add() can take only one argument. '''
s = {10, 20, 30}
s.add(40)
print(s) # {40, 10, 20, 30}
#--------------------------------------------------------
# set.update(x, y, z)
print("----- set.update(x, y, z) -----")
'''
- Add multiple item to set.
- Arguments are not individual elements they are iterable objects like list, range etc.
- All elements present in iterable object will be added.  '''
s = {10, 20, 30}
a = [40, 50, 60, 10]
s.update(a, range(5))
print(s) # {0, 1, 2, 3, 4, 40, 10, 50, 20, 60, 30}
#--------------------------------------------------------
# set.copy()
print("----- set.copy() -----")
'''
- Return shallow copy of set.
- Create new set but doesn't duplicate objects
- They are cloned object  '''
s = {10,20,30}
s1 = s.copy()
print(s1) # {10, 20, 30}
print(s1 is s) # False

print("---Shallow copy---")
mySet = {40, 10, 20, 30}
shallow_copy_mySet = mySet.copy()
print(mySet) # {40, 10, 20, 30}
print(shallow_copy_mySet) # {40, 10, 20, 30}
print(shallow_copy_mySet is mySet)  # False
shallow_copy_mySet.add(50)
print(mySet) # {40, 10, 20, 30}
print(shallow_copy_mySet) # {40, 10, 50, 20, 30}

print("---Deep copy---")
'''
- Create new set with new duplicate objects.
- Resulting in a completely independant copy.
'''
mySet = {10,20,30}
duplicate_set_mySet = mySet
print(mySet) # {10, 20, 30}
print(duplicate_set_mySet) # {10, 20, 30}

duplicate_set_mySet.add(40)
print(duplicate_set_mySet) # {40, 10, 20, 30}
print(mySet) # {40, 10, 20, 30}
print(duplicate_set_mySet is mySet) # True
#--------------------------------------------------------
# set.pop()
print("----- set.pop() -----")
# it removes and return some random element from set.
a = {11, 'jim', 44, 3.5, 2, 'Pam'}
a.pop() # 2 removed
print(a) # {3.5, 'jim', 'Pam', 11, 44}
print(a.pop()) # 3.5
print(a) # {'jim', 'Pam', 11, 44}
print(a.pop()) # jim
print(a) # {'Pam', 11, 44}
#--------------------------------------------------------
# set.remove(x)
print("----- set.remove(x) -----")
# it removes specified element from set.
a = {11, 'jim', 44, 3.5, 2, 'Pam'}
a.remove(44)
print(a) # {2, 3.5, 'Pam', 11, 'jim'}
# a.remove(10) # KeyError: 10
#--------------------------------------------------------
# set.discard(x)
print("----- set.discard(x) -----")
'''
- Like remove() it removes specified element from set.
- Unlike remove() if specified element not in present in set then also we won't get any error '''
a = {11, 'jim', 44, 3.5, 2, 'Pam'}
a.discard(44)
print(a) # {'jim', 2, 3.5, 'Pam', 11}
a.discard('10') 
print(a) # {'jim', 2, 3.5, 'Pam', 11}
#--------------------------------------------------------
# set.clear()
print("----- set.clear() -----")
# it removes all element from set.
a = {11, 'jim', 44, 3.5, 2, 'Pam'}
a.clear()
print(a) # set()
#--------------------------------------------------------
# Mathematical Operations on set
print("----- Mathematical Operations on set -----")
#--------------------------------------------------------
# set1.union(set2)
print("----- set1.union(set2) -----")
# Return all elements: (set1 | set2)
set1 = {10,20,30,40}
set2 = {30,40,50,60}
print(set1.union(set2)) # {40, 10, 50, 20, 60, 30}
print(set1 | set2) # {40, 10, 50, 20, 60, 30}
#--------------------------------------------------------
# set1.intersection(set2)
print("----- set1.intersection(set2) -----")
# Return common elements: (set1 & set2)
set1 = {10,20,30,40}
set2 = {30,40,50,60}
print(set1.intersection(set2)) # {40, 30}
print(set1 & set2) # {40, 30}
#--------------------------------------------------------
# set1.difference(set2)
print("----- set1.difference(set2) -----")
# Return elements in set1 not in set2: (set1 - set2)
set1 = {10,20,30,40}
set2 = {30,40,50,60}
print(set1.difference(set2)) # {10, 20}
print(set1 - set2) # {10, 20}
#--------------------------------------------------------
# set1.symmetric_difference(set2)
print("----- set1.symmetric_difference(set2) -----")
# Return elements either set1 or set2 but not both : (set1 ^ set2)
set1 = {10,20,30,40}
set2 = {30,40,50,60}
print(set1.symmetric_difference(set2)) # {10, 50, 20, 60}
print(set1 ^ set2) # {10, 50, 20, 60}
#--------------------------------------------------------
# Membership operators
print("----- Membership operators -----")
s = set("Jonathan")
print(s) # {'h', 'a', 'n', 't', 'o', 'J'}
print('J' in s) # True
print('h' not in s) # False
#--------------------------------------------------------
# Set comprehension
print("----- Set comprehension -----")
'''
- It is easy and compact way of creating set objects from any iterable objects.
- Syntax: set = [expression  for item in set  if condition]
'''
s = { x*10  for x in range(1,6,2) }
print(s) # {10, 50, 30}
#--------------------------------------------------------
#--------------------------------------------------------

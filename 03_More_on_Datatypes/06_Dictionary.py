# Dictionary
'''
- Dictionaries store data in key-value pairs.
- Unordered and Indexed collections of items in key-value pairs.
- Hetrogeneous objects are allowded for both keys and values.
- Mutable: Elements (key-value pairs) can be added, removed, or modified after creation.
- Keys are Unique: Each key in a dictionary must be unique.
- Key Types: Keys in a dictionary must be of an immutable data type
  such as strings, numbers, or tuples (containing only immutable elements). 
  This ensures that the keys can be hashed and used for efficient lookups.
- Dictionaries are created using curly braces {} with key-value pairs separated by colons (:).
- Dynamic: Dictionaries can grow or shrink in size as needed. 
  You can add new key-value pairs, remove existing ones, or modify the values associated with keys.
'''
#--------------------------------------------------------
# Creating dictionary
print("----- Creating dictionary -----")

# Empty dict
a = {}
print(a) # {}
print(type(a)) # <class 'dict'>

b = dict()
print(b) # {}
print(type(b)) # <class 'dict'>

# if we know emelents
marks = {"Java":95 , "Python":96 , "Django":95}
student = {101:"Jim" , 102:"Pam"}
print(marks) # {'Java': 95, 'Python': 96, 'Django': 95}
print(student) # {101: 'Jim', 102: 'Pam'}

# Using dict() function
a = [("day1",20) , ("day2",30) , ("day3",40)]
print(type(a)) # <class 'list'>
b = dict(a) 
print(b) # {'day1': 20, 'day2': 30, 'day3': 40}
print(type(b)) # <class 'dict'>
#--------------------------------------------------------
# Accessing data from dictionary
print("----- Accessing data from dictionary -----")
emp = {101:"Jim" , 102:"Pam", 103:"Micheal", 104:"Micheal", 105:"Dwight"}
print(emp[102]) # Pam
print(emp[104]) # Micheal
#--------------------------------------------------------
# Updating dictionary
print("----- Updating dictionary -----")
'''
- if key not available new key added.
- if key available old value will replaced by new value.
'''
emp = {101:"Jim" , 102:"Pam", 103:"Micheal"}
print(emp) # {101: 'Jim', 102: 'Pam', 103: 'Micheal'}
emp[104] = "Dwight"
print(emp) # {101: 'Jim', 102: 'Pam', 103: 'Micheal', 104: 'Dwight'}   
emp[102] = "Angela"
print(emp) # {101: 'Jim', 102: 'Angela', 103: 'Micheal', 104: 'Dwight'}
#--------------------------------------------------------
# Deleting elements from dictionary
print("----- Deleting elements from dictionary -----")
#--------------------------------------------------------
# del dict[key]
print("----- del dict[key] -----")
emp = {101:"Jim" , 102:"Pam", 103:"Micheal"}
print(emp) # {101: 'Jim', 102: 'Pam', 103: 'Micheal'}
del emp[103]
print(emp) # {101: 'Jim', 102: 'Pam'}
#del emp[400] # KeyError: 400
#--------------------------------------------------------
# dict.clear()
print("----- dict.clear() -----")
emp = {101:"Jim" , 102:"Pam", 103:"Micheal"}
print(emp) # {101: 'Jim', 102: 'Pam', 103: 'Micheal'}
emp.clear()
print(emp) # {}
#--------------------------------------------------------
# del dict
print("----- del dict -----")
emp = {101:"Jim" , 102:"Pam", 103:"Micheal"}
print(emp) # {101: 'Jim', 102: 'Pam', 103: 'Micheal'}
del emp
# print(emp) # NameError: name 'emp' is not defined
#--------------------------------------------------------
# Dictionary functions
print("----- Dictionary functions -----")
#--------------------------------------------------------
# dict()
print("----- dict() -----")
# To create dictionary
a = [("day1",20) , ("day2",30) , ("day3",40)]
print(type(a)) # <class 'list'>
b = dict(a) 
print(b) # {'day1': 20, 'day2': 30, 'day3': 40}
print(type(b)) # <class 'dict'>
#--------------------------------------------------------
# len()
print("----- len() -----")
# Returns number of items in dictionary
a = [("day1",20) , ("day2",30) , ("day3",40)]
print(len(a)) # 3
#--------------------------------------------------------
# dict.clear()
print("----- dict.clear() -----")
emp = {101:"Jim" , 102:"Pam", 103:"Micheal"}
print(emp) # {101: 'Jim', 102: 'Pam', 103: 'Micheal'}
emp.clear()
print(emp) # {}
#--------------------------------------------------------
# get()
print("----- get() -----")
'''
- To get value associated with key.
- dict.get(key) :
    if key available it return corresponding value otherwise return None.
- dict.get(key, default_value) :
    if key available it return corresponding value otherwise return default_value.
'''
emp = {101:"Jim" , 102:"Pam", 103:"Micheal"}
print(emp[102]) # Pam
# print(emp[400]) # KeyError: 400 
print(emp.get(102)) # Pam
print(emp.get("Jim")) # None
print(emp.get(400)) # None
print(emp.get(103, "Default")) # Micheal
print(emp.get(400, "Default")) # Default
#--------------------------------------------------------
# pop() 
print("-----dict.pop(key)-----")
'''
- Removes the entry associated with specified key and return the corresponding value.
- if specified key not available give key error. '''
emp = {101:"Jim" , 102:"Pam", 103:"Micheal"}
print(emp.pop(101)) # Jim
print(emp) # {102: 'Pam', 103: 'Micheal'}
# print(emp.pop()) # TypeError: pop expected at least 1 argument, got 0
# print(emp.pop(400)) # KeyError: 400
#--------------------------------------------------------
# dict.popitem() 
print("-----dict.popitem()-----")
# Removes last item (key-value) and return it.
emp = {101:"Jim" , 103:"Micheal", 102:"Pam"}
print(emp.popitem()) # (102, 'Pam')
print(emp) # {101: 'Jim', 103: 'Micheal'}

d = {} # Empty dictionary
# print(d.popitem()) # KeyError: 'popitem(): dictionary is empty'
#--------------------------------------------------------
# dict.keys() 
print("-----dict.keys()-----")
# Return all keys associated with dictionary.
emp = {101:"Jim" , 103:"Micheal", 102:"Pam"}
print(emp.keys()) # dict_keys([101, 103, 102])
for i in emp.keys():
  print(i) 
'''101
   103
   102'''
#--------------------------------------------------------
# dict.values() 
print("-----dict.values()-----")
# Return all values associated with dictionary.
emp = {101:"Jim" , 103:"Micheal", 102:"Pam"}
print(emp.values()) # dict_values(['Jim', 'Micheal', 'Pam'])
for i in emp.values():
  print(i) 
'''Jim
   Micheal
   Pam'''
#--------------------------------------------------------
# dict.items() 
print("-----dict.items()-----")
# Return list of tuples representing key value pair [(k,v),(k,v),(k,v)]
emp = {101:"Jim" , 103:"Micheal", 102:"Pam"}
print(emp.items()) # dict_items([(101, 'Jim'), (103, 'Micheal'), (102, 'Pam')])
for k,v in emp.items():
  print(k,"--",v)
'''101 -- Jim
   103 -- Micheal
   102 -- Pam'''
#--------------------------------------------------------
# dict.copy()
print("----- dict.copy() -----")
'''
- Return exactly duplicate dictionary (cloned copy/shallow copy)
- Create new dictionary but doesn't duplicate objects
- They are cloned object  '''
emp = {101:"Jim" , 103:"Micheal", 102:"Pam"}

shallow_copy_emp = emp.copy()
print(emp) # {101: 'Jim', 103: 'Micheal', 102: 'Pam'}
print(shallow_copy_emp) # {101: 'Jim', 103: 'Micheal', 102: 'Pam'}
print(shallow_copy_emp is emp) # False
shallow_copy_emp[104] = "Angela"
print(shallow_copy_emp) # {101: 'Jim', 103: 'Micheal', 102: 'Pam', 104: 'Angela'}
print(emp) # {101: 'Jim', 103: 'Micheal', 102: 'Pam'}
#--------------------------------------------------------
# dict.setdefault(k,v)
print("----- dict.setdefault(k,v) -----")
'''
- if key not available then specified key value will be added to dictionary.
- if key available then returns corresponding value.  '''
emp = {101:"Jim" , 103:"Micheal", 102:"Pam"}
print(emp.setdefault(104,"Angela")) # Angela
print(emp) # {101: 'Jim', 103: 'Micheal', 102: 'Pam', 104: 'Angela'}
print(emp.setdefault(101,"Dwight")) # Jim
print(emp) # {101: 'Jim', 103: 'Micheal', 102: 'Pam', 104: 'Angela'}
#--------------------------------------------------------
# dict1.update(dict2)
print("----- dict1.update(dict2) -----")
# all items present in dict2 will added to dict1.
dict1 = {1:11, 2:22, 3:33}
dict2 = {8:88, 9:99}
dict1.update(dict2)
print(dict1) # {1: 11, 2: 22, 3: 33, 8: 88, 9: 99}
print(dict2) # {8: 88, 9: 99}
#--------------------------------------------------------
# Dictionary comprehension
print("----- Dictionary comprehension -----")
'''
- It is easy and compact way of creating dictionary objects from any iterable objects.
- Syntax: dictionary = [expression  for item in dictionary  if condition]
'''
d = { x:x*10  for x in range(1,6) }
print(d) # {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}

squares = { i:i*i  for i in range(1,6)}
print(squares) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
#--------------------------------------------------------
#--------------------------------------------------------
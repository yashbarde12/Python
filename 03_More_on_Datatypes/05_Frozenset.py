# Frozenset
'''
- Frozenset is an immutable version of a set.
- Hashability: Unlike regular sets, frozenset instances are hashable. 
  This means that we can use a frozenset as a key in a dictionary or as an element in another set.
- Duplicate not allowed
- Hetrogeneous
- frozenset({})
- indexing not allowed
- insertaion order not preserved
'''
#--------------------------------------------------------
# Creating Frozenset
print("----- Creating Frozenset -----")

# If we know elements
s = ({10, 20, 30, 40})
print(s) # {40, 10, 20, 30}
print(type(s)) # <class 'set'>  # we must have to use function 

# Using frozenset() function
a = [10, 20, 30, 40, 10, 20, 10]
b = frozenset(a)
print(b) # frozenset({40, 10, 20, 30})
print(type(b)) # <class 'frozenset'>  

# Using iterable/range() function
s = frozenset(range(5))
print(s) # frozenset({0, 1, 2, 3, 4}) 
#--------------------------------------------------------
# Membership operators
print("---- Membership operators -----")
a = frozenset([1,2,3,4])
b = frozenset([3,4,5,6])
print(type(a)) # <class 'frozenset'>
print(2 in a) # True
print(4 not in b) # False
#--------------------------------------------------------
# len()
print("---- len() -----")
b = frozenset([3,4,5,6])
print(len(b)) # 4
#--------------------------------------------------------
# Iteration
print("---- Iteration -----")
a = frozenset([1,2,3,4])
for i in a:
    print(i)
'''1
   2
   3
   4'''
#--------------------------------------------------------
# Set operations on frozenset
print("---- Set operations on frozenset -----")
#--------------------------------------------------------
# fs1.union(fs2)
print("----- fs1.union(fs2) -----")
# Return all elements: (fs1 | fs2)
fs1 = frozenset({10,20,30,40})
fs2 = frozenset({30,40,50,60})
print(type(fs1)) # <class 'frozenset'>
print(fs1.union(fs2)) # frozenset({40, 10, 50, 20, 60, 30})
print(fs1 | fs2) # frozenset({40, 10, 50, 20, 60, 30})
#--------------------------------------------------------
# fs1.intersection(fs2)
print("----- fs1.intersection(fs2) -----")
# Return common elements: (fs1 & fs2)
fs1 = frozenset({10,20,30,40})
fs2 = frozenset({30,40,50,60})
print(fs1.intersection(fs2)) # frozenset({40, 30})
print(fs1 & fs2) # frozenset({40, 30})
#--------------------------------------------------------
# fs1.difference(fs2)
print("----- fs1.difference(fs2) -----")
# Return elements in fs1 not in fs2: (fs1 - fs2)
fs1 = frozenset({10,20,30,40})
fs2 = frozenset({30,40,50,60})
print(fs1.difference(fs2)) # frozenset({10, 20})
print(fs1 - fs2) # frozenset({10, 20})
#--------------------------------------------------------
# fs1.symmetric_difference(fs2)
print("----- fs1.symmetric_difference(fs2) -----")
# Return elements either fs1 or fs2 but not both : (fs1 ^ fs2)
fs1 = frozenset({10,20,30,40})
fs2 = frozenset({30,40,50,60})
print(fs1.symmetric_difference(fs2)) # frozenset({10, 50, 20, 60})
print(fs1 ^ fs2) # frozenset({10, 50, 20, 60})
#--------------------------------------------------------
# Frozenset comprehension
print("----- Frozenset comprehension -----")
'''
- It is easy and compact way of creating frozenset objects from any iterable objects.
- Syntax: fs = frozenset([expression  for item in froxenset  if condition])
'''
fs = frozenset({ x*10  for x in range(1,6,2) })
print(fs) # frozenset({10, 50, 30})
#--------------------------------------------------------
#--------------------------------------------------------


# Operators
'''
(ACALIMB)
1. Arithmatic
2. Comparison / relationship
3. Assignment
4. Logical
5. Identity
6. Membership
7. Bitwise

'''
#--------------------------------------------------------
# Arithmatic Operators: 
print("----- Arithmatic Operators -----")
'''
   + : Addition
   - : Subtraction
   * : Multiplication
   / : Division
  // : Floor division
  ** : Exponetial
   % : Modulus (Mod) 
'''

print('Addition ', 10+5) # Addition  15

print('Subtraction ', 10-5) # Subtraction  5

print('Multiplication ', 10*5) # Multiplication  50

print('Mod ', 10%2) # Mod  0

print('Exponetial ', 10**2) # Exponetial  100

print('Division ', 10/5) # Division  2.0
# in python, division always get floating result
print('Division ', 10.0/5) # Division  2.0
print('Division ', 10/3) # Division  3.3333333333333335

print('Floor division ', 10//3) # Floor division  3
print('Floor division ', 5//2)  # Floor division  2
print('Floor division ', 10//5) # Floor division  2
print('Floor division ', 10.0//5) # Floor division  2.0
print('Floor division ', -10//2) # Floor division  -5
print('Floor division ', -10//3) # loor division  -4

print('Result: ', True+True) # Result:  2
# internally PVM consider True as 1 and False as 0

#--------------------------------------------------------
# Comparison / relationship Operators: 
print("----- Comparison Operators -----")
'''
   > : Greater than
   < : Less than
   >= : Greater than equal to
   <= : Less than equal to
'''

a = 10
b = 20
print("a > b : ", a > b) # a > b :  False
print("a < b : ", a < b) # a < b :  True
print("a >= b : ", a >= b) # a >= b :  False
print("a <= b : ", a <= b) # a <= b :  True

#--------------------------------------------------------
# Assignment Operators: 
print("----- Assignment Operators -----")
'''
   =  : Equal to
   += : Increment
   -= : Decrement
   *= : Multiple equal to
   /= : Division equal to
'''

x = 10
print(x) # 10
x = x+5 
print(x) # 15


a = 5
a += 2 # a += 2 means a = a + 2 
print(a) # 7

b = 15
b -= 5 # b -= 5 means b = b - 5 
print(b) # 10

c = 2
c *= 3 # c *= 3 means c = c * 3 
print(c) # 6

d = 50
d /= 5 # d /= 5 means d = d / 5 
print(d) # 10.0

#--------------------------------------------------------
# Logical Operators: 
print("----- Logical Operators -----")
'''
   and : only returns True if all conditions are True
   or  : only returns False if all conditions are False
   not : reverse the result
'''
# and 
print(10>5 and 10>2) # True
print(10<5 and 10>2) # False

# or 
print(10>5 or 10>2) # True
print(10<5 or 10>2) # True

#not 
print(not True) # False

#--------------------------------------------------------
# Identity Operators: 
print("----- Identity Operators -----")
'''
- We use for address comparision
   1. is  
   2. is not 
'''
p = 20
q = 20
print(id(p)) # 2231247176528
print(id(q)) # 2231247176528 # reusabilty
print(p is q) # True
print(p is not q)  # False

q = 50
print(id(q)) # 2231247177488 # immutability
print(p is q) # False
print(p is not q) # True

#--------------------------------------------------------
# Membership Operators: 
print("----- Membership Operators -----")
'''
- We use to check given object is present in given collection
   1. in  
   2. not in
'''
list = ['Micheal', 'Jim', 'Pam', 'Dwight']
print('sunny' in list ) # False
print('Jim' in list ) # True
print('Jim' not in list ) # False

#--------------------------------------------------------
# Bitwise Operators: 
print("----- Bitwise Operators -----")
'''
   & : Bitwise and (if both bits are 1 then only result is 1 otherwise 0)
   | : Bitwise or (if atleast one bit is 1 then result is 1 otherwise 0)
   ^ : Multiplication (if bits are different then only result is 1 otherwise 0)
   ~ : Bitwise not (complement)
  << : Bitwise left shift 
  >> : Bitwise right shift 
'''
print(12 & 6) # 4
print(12 | 6) # 14
print(12 ^ 6) # 10
print(~ 6) # -7
print(~ 135) # -136
print(12 >> 3) # 1
print(12 << 2) # 48

#--------------------------------------------------------
#--------------------------------------------------------

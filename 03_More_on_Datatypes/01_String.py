# Strings
'''
- Any Sequence of characters within either single, double or triple quote considered as string.
- string in python stored as individual characters i.e. indexed wise.
- Index by default start with 0.
- Indexing: 1. forward indexing start with 0
            2. backward indexing start with -1
            Example: str = "python"

                     0   1   2   3   4   5
                     p   y   t   h   o   n
                    -6  -5  -4  -3  -2  -1 
- Strings are immutable,
  hence you caannot change the individual letters of string using assignment operator.
'''
#--------------------------------------------------------
name, age = "Jim", '36'
name2 = ''' A
            s
            h'''
print(type(name)) # <class 'str'>
print(type(age)) # <class 'str'>
print(type(name2)) # <class 'str'>
'''
f = "Hello python' 
print(f) # Error # string must start and end with same quotes.'''
#--------------------------------------------------------
# String Operators
print("----- String Operators -----")
'''
1. Concatenation Operator : +
2. Replication Operator   : *
3. Membership Operators   : (in / not in)
4. Comparison Operators   : (<,>,<=,>=,==,!=)
'''
x = 'Every' + 'day'
print(x) # Everyday

x = 'Hello' * 3
print(x) # HelloHelloHello

print('a' in 'Pam') # True
print('a' not in 'Pam') # False

print('a' == 'a') # True
print('Pam' == 'Pam') # True
print('a' != 'Pam') # True
print('a' != 'A') # True
print('pam' == 'Pam') # False
print('PAM' == 'pam') # False
print('a' > 'A')  # True #ASSCII value a : 97 and A : 65
#--------------------------------------------------------
# String Slicing
print("----- String Slicing -----")
'''
- Slicing : selecting subpart/substring between n and m
            starting at n, n+1, n+2,...till m-1
- Syntax :  Variable_name [start : end : step_value]
'''
a = "Hello World"
print(a[4:-2]) # o Wor
print(a[6:], a[:6]) # World Hello 
'''
step 1 : Check sign of step value
step 2 : if Positive then indexing if forward, start from 0 
         if Negative then indexing if backward, start from -1 
step 3 : if step value is 2 then skip 1 character 
         i.e no of skip characters = step value -1
'''
s = "maharashtra"
print(s[2:8:2]) # hrs
print(s[2:-4:2]) # hrs
print(s[-5:1:3]) # 
print(s[6:1:-1]) # sarah
print(s[::-1]) # arthsaraham
#--------------------------------------------------------
# Built-in functions of string
print("----- Built-in functions of string -----")
#--------------------------------------------------------
# len() 
print("-----len()-----")
''' This function returns the length of string. '''
a  = "Hello Python"
print("length of string is:",len(a)) # length of string is: 12

a = 'Jim' # Jim
for i in range(0, len(a)):
    print(a[i], end='') # Jim
print() 
#--------------------------------------------------------
# capitalize() 
print("-----capitalize()-----")
''' This function returns copy of string with its first charater capitalized. '''
a = "hello Python"
print(a.capitalize()) # Hello python
#--------------------------------------------------------
# isupper() 
print("-----isupper()-----")
a , b = "Python", "PYTHON"
print(a.isupper()) # False
print(b.isupper()) # True
#--------------------------------------------------------
# islower() 
print("-----islower()-----")
a , b = "python", " "
print(a.islower()) # True
print(b.islower()) # False
#--------------------------------------------------------
# swapcase() 
print("-----swapcase()-----")
a = "learning Python is very Easy"
print(a.swapcase()) # LEARNING pYTHON IS VERY eASY
#--------------------------------------------------------
# title() 
print("-----title()-----")
a = "learning Python is very Easy"
print(a.title()) # Learning Python Is Very Easy
#--------------------------------------------------------
# find() 
print("-----find()-----")
''' 
- Returns the lowest index in string where the substring is found.
- returns lowest index where it is found and if not found it returns -1 '''
a = "JIM IS GOING TO MARKET"
b = "TO"
print(a.find(b, 0 , len(a)-1)) # 13
#--------------------------------------------------------
# isalnum()
print("-----isalnum()-----")
'''
- This returns True if characters in string are alphanumeric
  and there is atleast one character otherwise it return False''' 
a = 'jim123'
b = 'hello'
c = '123456'
d = ''
print(a.isalnum()) # True
print(b.isalnum()) # True
print(c.isalnum()) # True
print(d.isalnum()) # False
#--------------------------------------------------------
# isdigit()
print("-----isdigit()-----")
'''
- This returns True if all characters in string are digits
  and there is atleast one digit otherwise it return False''' 
a = 'jim123'
b = 'hello'
c = '123456'
d = ''
print(a.isdigit()) # False
print(b.isdigit()) # False
print(c.isdigit()) # True
print(d.isdigit()) # False
#--------------------------------------------------------
# isalpha()
print("-----isalpha()-----")
a = 'jim123'
b = 'hello'
c = '123456'
d = ''
print(a.isalpha()) # False
print(b.isalpha()) # True
print(c.isalpha()) # False
print(d.isalpha()) # False
#--------------------------------------------------------
# isspace()
print("-----isspace()-----")
'''
- This returns True when there are only white spaces in string
  and there is atleast one character otherwise it return False'''
a = ' '
b = ''
print(a.isspace()) # True
print(b.isspace()) # False
#--------------------------------------------------------
# lstrip()
print("-----lstrip()-----")
s1 = "        python"
print(s1.lstrip()) # python
#--------------------------------------------------------
# rstrip()
print("-----rstrip()-----")
s2 = "python           "
print((s2.rstrip())) # python
#--------------------------------------------------------
# strip()
print("-----strip()-----")
s3 = "    python     "
print(s3.strip()) # python
print(len(s3)) # 15
print(len(s3.strip())) # 6
#--------------------------------------------------------
# count()
print("-----count()-----")
# Return the number of non-overlapping occurrences of substring
str = 'abcabcabcabcadda'
print(str.count('a')) # 6
print(str.count('ab')) # 4
print(str.count('a', 3, 7)) # 2
#--------------------------------------------------------
# replace()
print("-----replace()-----")
str = "Learning python is very difficult."
print(str.replace("difficult", "easy")) # Learning python is very easy.

print(str) # Learning python is very difficult. 
# we can see if we print original string again it's not changed, cause strings are immutable.
#--------------------------------------------------------
# split()
print("-----split()-----")
# Return a list of the substrings in the string, using sep as the separator string.
date , str = "8-11-2023" , "abc de fgh"
splited_date = date.split("-") 
print(date) # 8-11-2023
print(splited_date) # ['8', '11', '2023']
print(str.split()) # ['abc', 'de', 'fgh']
#--------------------------------------------------------
# seperator.join()
print("-----seperator.join()-----")
print("---".join(splited_date)) # 8---11---2023
str = 'ab', 'abc', 'xyz'
print('/'.join(str)) # ab/abc/xyz
#--------------------------------------------------------
# startswith()
print("-----startswith()-----")
a = "learning Python is very easy"
print(a.startswith("Python")) # False
print(a.startswith("learning")) # True
#--------------------------------------------------------
# endswith()
print("-----endswith()-----")
a = "learning Python is very easy"
print(a.endswith("Python")) # False
print(a.endswith("easy")) # True
#--------------------------------------------------------
# format()
print("-----format()-----")
name, salary, age = 'Jim', '30000', '28'
print("{}'s salary is {} rupees and he is {} years old.".format(name, salary, age)) 
# Jim's salary is 30000 rupees and he is 28 years old.

#--------------------------------------------------------
#--------------------------------------------------------

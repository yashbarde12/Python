# Identifiers and Variables
'''
Identifiers:
    - A Name in python program is called identifier.
    - It can be class name, function name, module name or variable name.
    - There is no limit for python identifiers but not recommend to use lenghthy identifiers.
    - Ex.   class Student:
                  pass
      here Student is identifier.

Variables:
    - Variables are names given to data that we need to store and manipulate in our programs. 
'''
#--------------------------------------------------------
# Variables

print("Welcome")
name = "Yash" # name is variable
print(name)

#--------------------------------------------------------
a=10
b=20
print(a,b)

#--------------------------------------------------------
p,q,r = 55,66,77 # We can also define multiple variables at one go.
print(p,q,r)
print(p,q,r,sep=",")
print(p,q,r,sep="-")

#--------------------------------------------------------
x=y=50 
print(x,y)

#--------------------------------------------------------
# 5age = 20 # SyntaxError: invalid decimal literal
# age$ = 30  # SyntaxError: invalid decimal literal
# @age = 20 # SyntaxError: invalid syntax
#--------------------------------------------------------

#Deleting variables
my_name = 'Yash'
print("variable my_name: ",my_name)
del my_name
#print("variable my_name: ",my_name) #Error

#--------------------------------------------------------
#--------------------------------------------------------

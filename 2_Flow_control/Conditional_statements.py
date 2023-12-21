# Conditional Statements
'''
- If statements are used for conditional execution in Python.
- They allow you to execute a block of code only if a certain condition is true.

- Types:
    1. if 
    2. if - else
    3. if - elif - else
'''
#--------------------------------------------------------
# if statement
'''
syntax: 
    if expression:
            statement1
            statements 2 
'''

num = int(input("Enter any number: "))

if num % 2 == 0:    
    print("Number is even") 

#--------------------------------------------------------
# if else statement
'''
Syntax:
    if expression:
            statements
    else:
            statements  
'''

num = int(input("Enter any number: "))

if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

#--------------------------------------------------------
# if elif else statement
'''
Syntax:
    if expression:
            statements
    elif expression:
            statements
    elif expression:
            statements
    else:
            statements 
'''

marks = int(input("Enter total marks of student: "))

if marks >= 65:
    print("Distinction")
elif marks < 65 and marks >= 60:
    print("First Class")
elif marks < 60 and marks >= 50:
    print("Second class")
elif marks < 50 and marks >= 40:
    print("Just passing marks")
else:
    print("Failed") 
   
#--------------------------------------------------------
#-------------------------------------------------------- 





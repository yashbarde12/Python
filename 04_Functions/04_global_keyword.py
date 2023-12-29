# global keyword
'''
- we can use global keyword for this purposes:
- To declare global variable inside function.
- To make global variable available to function so we can perform required modification.
'''
#--------------------------------------------------------
def add(x,y):
   name = "raj" # Here name is local varibale
   result = x + y # Here result is local variable for function add.
   print(result) # 30
   
add(10,20)
# print(result) # NameError: name 'result' is not defined
#--------------------------------------------------------
# global keyword
print("----- global keyword -----")
#--------------------------------------------------------
# Use 1 : declaring global variable inside function
print("----- case 1 -----")
def sub(x,y):
   global sub_result # declaring global variable inside function
   sub_result = x - y
   print(sub_result) # 15
   
sub(20,5)
print("Accessing sub_result outside a function :", sub_result)
# Accessing sub_result outside a function : 15
#--------------------------------------------------------
# Use 2 : To change already existing global varible's values inside a function
print("----- case 2 -----")
age = 30
def change_age():
   global age
   age = 40
   print("Age inside a function :",age) 
   # Age inside a function : 40
change_age()
print("Age outside a function :",age) 
# Age outside a function : 40
#--------------------------------------------------------
print("----- case 3 -----")
# without using global keyword
a = 10 
def f1():
    a = 777 
    print(a) # 777

def f2():
    print(a) # 10

f1() 
f2()
# same with using global keyword
a = 10 
def f1():
    global a
    a = 777 
    print(a) # 777

def f2():
    print(a) # 777

f1() 
f2()
#--------------------------------------------------------
# if name of local and global variable is same
# Then  more priority given to local variable inside function.
print("----- case 4 -----")
city = "Mumbai" # global variable
def place():
   city = "Delhi" # local variable
   print("City inside function: ",city) # City inside function: Delhi
   print(globals()['city']) # Mumbai

place()
print("City outside function: ",city) # City outside function: Mumbai
#--------------------------------------------------------
#--------------------------------------------------------
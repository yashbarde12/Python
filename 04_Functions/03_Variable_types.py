# Types of variables
'''
Python support 2 types of variables:
        1. Local variable.
        2. Global variables.
'''
#--------------------------------------------------------
# Local variables
print("----- Local variables -----")
'''
- Varibles declare inside function are Local variables.
- Available only for function in which they are declared.  '''
def f1():
    a = 10 # Here a cannot be access outside fun1() function.
    print(a) # Hence a is local variable of fun1() function.

def f2():
    print(a) # Invalid

f1() # 10
# f2() # NameError: name 'a' is not defined
#--------------------------------------------------------
# Global variables
print("----- Global variables -----")
'''
- Varibles declare outside function are global variables.
- They can access in all functions of module.    '''
a = 10 # a is global variable
def fun1():
    print(a) # 10 
    print(b) # Jim
b = "Jim" # b is global variable
def fun2():
    print(a) # 10 
    print(b) # Jim

fun1()
fun2()
#--------------------------------------------------------
#--------------------------------------------------------

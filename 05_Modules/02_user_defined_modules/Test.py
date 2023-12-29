# Only uncomment (""" """)each section before executing for understanding.
"""
import Calci_module
print(Calci_module.name)
print("Addition:", Calci_module.add(10,20)) # Addition: 30 
''' Output:
    value of __name__: Calci_module
    This file executed by some other file as a module.
    jim
    Addition: 30 '''
"""
#--------------------------------------------------------
"""
# case 1
print("---- case 1 -----")
from Calci_module import add
print("Addition:", add(20,60)) # Addition: 80
# print("Subtraction:", sub(30,10)) # NameError: name 'sub' is not defined. 
"""
#--------------------------------------------------------
"""
# case 2 : 
print("---- case 2 -----")
from Calci_module import sub, name
print("Subtraction:", sub(20,7)) # Subtraction: 13
print(name) # jim
# print("Addition:", add(20,60)) # NameError: name 'add' is not defined
"""
#--------------------------------------------------------
"""
# case 3
print("---- case 3 -----")
from Calci_module import *
print("Subtraction:", sub(20,7)) # Subtraction: 13
print(name) # jim
print("Addition:", add(20,60)) # Addition: 80
"""
#--------------------------------------------------------
"""
# case 4
print("---- case 4 -----")
import Calci_module as calculator
# print(Calci_module.add(10,20)) # NameError: name 'Calci_module' is not defined
print("Addition:", calculator.add(30,10)) # Addition: 40
"""
#--------------------------------------------------------
"""
# case 5
print("---- case 5 -----")
from Calci_module import add as addition
# print("Addition:", add(30,78)) # NameError: name 'add' is not defined
print("Addition:", addition(30,78)) # Addition: 108
"""
#--------------------------------------------------------
"""
from Calci_module import add as  addition, sub as subtraction
# print("Subtraction:", sub(20,7)) # NameError: name 'sub' is not defined.
# print("Addition:", add(20,60)) # NameError: name 'add' is not defined
print("Addition:", addition(20,7)) # Addition: 27
print("Subtraction:", subtraction(20,60)) # Subtraction: -40
"""
#--------------------------------------------------------

import Calci_module
# print(help(Calci_module))
'''Output:
        Help on module Calci_module:
        NAME
            Calci_module
        FUNCTIONS
            add(x, y)
            sub(x, y)
        DATA
            name = 'jim'
        FILE
            i:\my drive\itvedant\python\my python_notes\05_modules\02_user_defined_modules\calci_module.py
        None   '''
print(dir(Calci_module))
'''Output:
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
 '__name__', '__package__', '__spec__', 'add', 'name', 'sub']   '''

#--------------------------------------------------------
#--------------------------------------------------------
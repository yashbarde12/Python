# OOP (Object Oriented Programming):
# Way of writting a program which includes classes, objects,... etc
#--------------------------------------------------------
# Class:
'''
- A class is a blueprint for creating objects (instances).
- Class is a logical entiry with some specific properties and behaviours. it is a collection of objects.
- Properties / Attributes : Variables 
- behaviours              : Methods (Functions) 
- Example: Employee is a class with attributes Name, age, Salary, Position, Department
  so each employee details is treated as an object   '''
#--------------------------------------------------------
# Class Creation
'''
- Class is created by using class keyword.
- Class name must start with capital letter.
- Syntax:
        class Class_name:
                statement 1
                statement 2
'''
#--------------------------------------------------------
# Objects (Instances)
'''
- Object is an instance of a class.
- Each object created from a class has its own unique set of attributes 
  and can perform actions (methods) defined in the class.
- Syntax:
        Object_name = Class_name(Arguments)
- Example:
        class Student: 
            rollno = 10
            name = "Jim"

        a = Student() # Here Student() is a object/instance
                      # Here a is reference variable
- Reference variable: variable which can be used to refer objects.
  using reference variable we can access properties and method of objects.
'''
#--------------------------------------------------------
# Properties/ Attributes
'''
- Attributes are variables that belong to a class or an object.
- They represent the state of the object and can be data variables or class variables. 
'''
#--------------------------------------------------------
# Methods/ behavior
'''
- Methods are functions defined within a class.
- They define the behavior or actions that objects of the class can perform.
- Methods can interact with attributes of the class
'''
#--------------------------------------------------------
# classes and objects
print("----- classes and objects -----")
class Car:  # class
   name = "Honda" # variable
   milage = 35    # variable
   
   def engine(self):  # Method / behaviour
      # self is pointing towards currenct object
      print("self:", self)
      print("Car is cool.")

Car()  # Object # This is useless object
c1 = Car() # c1 is reference variable, pointing to object Car()

print(c1.name) 
print(c1.milage) 
c1.engine()

Car().engine() # calling method without reference variable.
''' Output:
    Honda
    35
    self: <__main__.Car object at 0x000001A331D0BB80>
    Car is cool.
    self: <__main__.Car object at 0x000001A331D0BA90>
    Car is cool.   '''
'''
when object is created, it brodcasts it reference and it is duty of every 
method present inside class to receive and store that refernce for future use.
'''   
#--------------------------------------------------------
# Deleting an object
print("----- Deleting an object -----")
# del keyword is used for deleting an object or its properties.

class Student:  
    rollno = 10  
    name = "Jim"  
  
    def display(self):  
        print("Roll no: %d \nName: %s" %(self.rollno, self.name))  
    
    # del name
    
st1 = Student()
st1.display()  
''' Output:
    Roll no: 10
    Name: Jim    '''

# del st1  # Deleting the object itself
# st1.display() # NameError: name 'st1' is not defined.
#--------------------------------------------------------
#--------------------------------------------------------






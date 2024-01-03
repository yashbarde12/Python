# Constructors
''' 
- Special type of method which is used to initialize the instance of a class.
- It it called as magic method, because, it get excecutes automatically when object is created.
- Used to assign values to the data members of the class when an object of class is created. 
- constructor is having fixed name i.e __init__(self)
- self must be first parameter of costructor.
- consteructor is used to intialize instance varibale.
- if we are not providing any constructor, then python provides its default constructor.
'''
#--------------------------------------------------------
# __init__() method:
print("----- __init__() method ------")
print("----- Example 1 ------")
# It is called when the class is instantiated and used to initialize the class attributes.

class Student:
    def __init__(self, rollno, name, age):
        self.rollno = rollno
        self.name = name
        self.age = age
    def display(self):
        print("Roll No.:", self.rollno)
        print("Name    :", self.name)
        print("Age     :", self.age)
        
st1 = Student(101, "Jim", 20)
st2 = Student(102, "Pam", 21)
st3 = Student(103, "Dwight", 25)

st1.display()
st2.display()
st3.display()
''' Output:
    Roll No.: 101
    Name    : Jim
    Age     : 20
    Roll No.: 102
    Name    : Pam
    Age     : 21
    Roll No.: 103
    Name    : Dwight
    Age     : 25 '''
#--------------------------------------------------------
print("----- Example 2 ------")
class Employee:
   institute = "Terna"
   
   def __init__(self, name, phone):
      print("id of self :", id(self))
      self.emp_name = name  #instance variable
      self.emp_phone = phone #instance variable
      
   def display(self):
      print("Displaying name of employee:", self.emp_name)
      
      
jim = Employee("Jim","8698562365")
print("id of emp_1:", id(jim))

pam = Employee("Pam","8698562345")
print("id of emp_2:",id(pam))

# print(jim.name) # AttributeError: 'Employee' object has no attribute 'name'
print(jim.emp_name)
print(pam.emp_name)
print(pam.emp_phone)

jim.display() # Displaying name of employee: Jim
pam.display() # Displaying name of employee: Pam
 
print(jim.__dict__) # {'emp_name': 'Jim', 'emp_phone': '8698562365'} # all instance variables.
print(Employee.__dict__) #all class variables
#--------------------------------------------------------
print("----- Example 3 ------")
# Using different self parameters:
class Student:
    def __init__(self1, rollno, name, age):
        self1.rollno = rollno
        self1.name = name
        self1.age = age
    def display(self2):
        print("Rollno: %d \nName: %s \nAge: %d" %(self2.rollno, self2.name, self2.age))

st1 = Student(105, "Angela", 19)
st1.display()
''' Output:
Rollno: 105
Name: Angela
Age: 19 '''

# Count no of objects in a class
class Student:    
    count = 0    
    def __init__(self):    
        Student.count = Student.count + 1
        
st1=Student()    
st2=Student() 
# print("The number of students:",Student.count) # The number of students: 2
st3=Student()   
print("The number of students:",Student.count) # The number of students: 3
#--------------------------------------------------------
print("----- Types of constructors ------")
'''
1. Non - Parameterized constructor
2. Parameterized constructor   '''
#--------------------------------------------------------
print("----- Non - Parameterized constructor ------")
# It is used when we do not want to manipulate the value or the constructor that has only self as an argument.
class Student:  
    def __init__(self):  
        print("This is non parametrized constructor.")  
    def display(self, rollno, name):  
        print("Rollno: ", rollno, " Name: ",name)
        
st = Student() # This is non parametrized constructor.
st.display(106, "Jim") # Rollno:  106  Name:  Jim
#--------------------------------------------------------
print("----- Parameterized constructor ------")
class Student:
    def __init__(self1, rollno, name, age):
        self1.rollno1 = rollno   #rollno1 = 106
        self1.name1 = name      #name1 = "Andy"
        self1.age1 = age
    def display(self1):
        print("Rollno: %d \nName: %s \nAge: %d" %(self1.rollno1, self1.name1, self1.age1))

st1 = Student(106, "Andy", 20)
st1.display()
''' Output:
    Rollno: 106
    Name: Andy
    Age: 20  '''
#--------------------------------------------------------
# Multiple constructors in a class
''' 
- The constructor overloading is not allowed in Python.
- The object of the class always calls the last constructor if the class has multiple constructors.  '''
print("----- Overloading -----")
class Student:  
    def __init__(self):  
        print("The First Constructor")  
    def __init__(self):  
        print("The second Contructor")  
  
st = Student() # The second Contructor
#--------------------------------------------------------
#--------------------------------------------------------

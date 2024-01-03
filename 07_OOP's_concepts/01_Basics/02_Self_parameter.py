# Self parameter
''' 
- The self-parameter refers to the current instance of the class
  and accesses the class variables
- It must be the first parameter of any function which belongs to the class.
- self is not a keyword. its just a word, you can use anything instead of self.
- self must be first parameter of a instance method in OOP.
- self must be first parameter of constructor.
'''
#--------------------------------------------------------
class Student:
    rollno = 10
    name = "Jim"

    def display(self):
        print("Name:", self.name) # Name: Jim  
        print("Roll no:", self.rollno) # Roll no: 10

st = Student() # Creating object Student()
st.display() # calling method display()
#--------------------------------------------------------
class Person:
   def walking(self):
      print("self reference is:",id(self)) 
      print("person is walking.") 
      
p1 = Person()
print("p1 reference is :",id(p1)) 
p1.walking()

p2 = Person()
print("p2 reference is :",id(p2)) 
p2.walking()
''' p1 reference is : 2522434943824 
    self reference is: 2522434943824
    person is walking
    p2 reference is : 2522434943776 
    self reference is: 2522434943776
    person is walking    '''
#--------------------------------------------------------
#--------------------------------------------------------


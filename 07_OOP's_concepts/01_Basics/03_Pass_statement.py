# pass Statement
''' 
Class definitions cannot be empty, 
but if we want class definition with no content for some reason,
we can put in the pass statement to avoid getting an error. 
'''
#--------------------------------------------------------
class Student:
    pass

class Student:
    def __init__(self,r,n):
        self.rollno = r
        self.name = n
        print("Student detail")
    
    def display(para): # using para instead of self
        print("Roll no: %d \nName: %s" %(para.rollno, para.name))


ob1 = Student(10, "Pam")
ob1.display()
''' Output:
    Student detail
    Roll no: 10
    Name: Pam  '''
#--------------------------------------------------------
#--------------------------------------------------------
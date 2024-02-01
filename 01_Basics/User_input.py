# User Input
'''
- input()
- Take input from user.
- Default datatype given by input() function is string 
'''
#--------------------------------------------------------
Name = input("Enter your name : ") 
Age = input("Enter your age : ") 

print(type(Name)) # <class 'str'>  
print(type(Age)) # <class 'str'> 

#--------------------------------------------------------
a = input("Enter 1st number: ") 
b = input("Enter 2nd number: ") 
result = a + b 
print("Addition is : ", result) # Addition is :  25

'''
Here the result 52 becuase default datatype is string.
if we use + on string, it perfroms concatination.
'''

#--------------------------------------------------------
#--------------------------------------------------------
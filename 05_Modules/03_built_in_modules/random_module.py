# Random Module
'''
- This module define several functions to generate random numbers.
- We can use these functions while developing some games.
'''
#--------------------------------------------------------
from random import *
#--------------------------------------------------------
# random() 
print("-----random()-----")
# Return random float values between 0 and 1 (not inclusive).
a = random()
print(a) # 0.6987015218447455
for i in range(3):
    print(random())
    ''' output:
        0.919615519700859 
        0.8741972333262698
        0.5312840205803371 '''
#--------------------------------------------------------
# randint(range) 
print("-----randint()-----")
# Return random integer in range [a, b], including both end points.
print(randint(10,20)) # 16

for i in range(3):
    print(randint(100,500))
    ''' output:
        246
        410
        249 '''
#--------------------------------------------------------
# uniform(range) 
print("-----uniform()-----")
# Return random float values between two numbers (not inclusive).
print(uniform(10,20)) # 13.613875720728656

for i in range(3):
    print(uniform(100,500))
    ''' output:
        498.39349079510964
        360.5428635551389
        257.3923452294623 '''
#--------------------------------------------------------
# randrange(range) 
print("-----randrange()-----")
# Return a random item from range(start, stop, step). # start <= x < stop
print(randrange(10,20)) # 10

for i in range(6):
    print(randrange(10,15,2))
    ''' output:
        10
        10
        10
        14
        12
        14 '''
#--------------------------------------------------------
# choice() 
print("-----choice()-----")
# Return a random element from a non-empty sequence.. # start <= x < stop
mylist = [1, 0.56, [4,2], 'Pam']
print(choice(mylist)) # Pam
for i in range(5):
    print(choice(mylist))
    ''' output:
        Pam
        1
        [4, 2]
        0.56
        [4, 2] '''
#--------------------------------------------------------
#--------------------------------------------------------
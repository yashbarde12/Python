# Iterative Statements
'''
- Execute a group of statements multiple times then we should go for iterative statements.
    1. for loop
    2. while loop
'''
#--------------------------------------------------------
# for loop
print("----- for loop -----")
'''
- if we want to execute some action for every element present in sequence.
- The for loop in Python is primarily used for iterating over sequences like lists, tuples, strings, and dictionaries.
- Syntax:
            for iterative_variable in sequence:
                                        statements 
'''
L1 = [10,20,30.40,50]
print(L1) # [10, 20, 30.4, 50]

for i in L1:
    print(i)   
''' 
10
20
30.4
50    
'''

str = "Terna"
print(str) # Terna
for i in str:
    print(i, end="-") # T-e-r-n-a-
print()
#--------------------------------------------------------
# range() function
'''
- The range() function generates a sequence of numbers that can be used in for loops.
- It's commonly used to iterate a specific number of times.
- Syntax: range(start, stop, step value)
'''
print(list(range(1,6,1))) # [1, 2, 3, 4, 5]   
print(list(range(1,6))) # [1, 2, 3, 4, 5]   
print(tuple(range(1,6,1))) # (1, 2, 3, 4, 5)   
print(list(range(1,6,2))) # [1, 3, 5]
print(list(range(5,10,-1))) # []
print(list(range(10,5,-1))) # [10, 9, 8, 7, 6]  

num = int(input("Enter the number: ")) # Enter the number: 3
for i in range(1,11):
    print(num, "*", i, "=", num*i)
'''
3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
3 * 6 = 18
3 * 7 = 21
3 * 8 = 24
3 * 9 = 27
3 * 10 = 30
'''

#--------------------------------------------------------
# While loop
print("----- while loop -----")
'''
- Execute a group of statements iteratively until some condition become false.
- Syntax:
            while condition:
                    statement
'''

str = "terna"
i = 0
while i < len(str):
    print(str[i]) 
    i+=1
'''
t
e
r
n
a
'''

#--------------------------------------------------------
#--------------------------------------------------------

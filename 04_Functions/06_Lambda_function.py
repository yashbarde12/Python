# Lambda Function / Anonymous Function
'''
- Sometimes we can declare a function without any name.
- Such type of nameless functions are called Anonymous or Lambda functions.
- lambda keyword is used to declare this function.
- Syntax:
            lambda arguments : expression
'''
#--------------------------------------------------------
print("----- Normal Function -----")
def squareit(n):
    return n * n
a = squareit(3)
print(a) # 9
#--------------------------------------------------------
print("----- Lambda Function -----")
# printing square of number
a = lambda n : n*n
print(a(3)) # 9

# printing sum of two numbers
sum = lambda a,b : a + b
print(sum(3, 2)) # 5
#--------------------------------------------------------
# Using filter() function
print("----- filter(function, sequence) -----")
''' 
- We can use filter() function to filter values from given sequence based on condition.
- It accepts a function and a sequence as an argument.
- Used to filter out all elements of the sequence returning the new sequence 
- filter(function, sequence)'''

a = [10,22,37,41,100,123,29]
evenlist = list(filter(lambda x : (x%2 == 0), a))
print(evenlist) # [10, 22, 100]
#--------------------------------------------------------
# Using map() function
print("----- map(function, sequence) -----")
# It accepts a function and a sequence as an argument. 

t1 = (10,20,30,40,50,60)  
square = list(map(lambda x : x**2, t1))   
print(square) # [100, 400, 900, 1600, 2500, 3600]  
#--------------------------------------------------------
#--------------------------------------------------------
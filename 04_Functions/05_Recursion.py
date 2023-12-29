# Recursion
'''
- Functions can call themselves, enabling a technique known as recursion.
- Functions can call itself its known as recursive function.
- Recursion is useful for solving problems that can be broken down into smaller, similar sub-problems.
- Advantage of recursive function:
        1. We can reduce length of code and improves readability.
        2. We can solve complex programs very easily.
'''
#--------------------------------------------------------
# Printing 1 to 5 numbers using recursion.
print("Printing 1 to 5 numbers using recursion.")
def recursion(start, end):
    if(start <= end):
       print(start)
       start = start + 1
       recursion(start, end)

recursion(1,5)
''' 1
    2
    3
    4
    5 '''
#--------------------------------------------------------
# Program to calculate factorial of a number.
print("Program to calculate factorial of a number.")
# 3! = 3 * 2! then n! = n * (n-1)!

def fact(n):  
    if n == 0 or n == 1:  
        return 1
    elif n < 0:
        return print("Factorial of negative numbers not exist.")  
    else:  
        return n * fact(n - 1)  
  
a = int(input("Enter a number: ")) # Enter a number: 3
print("Factorial of ", a, "is", fact(a)) # Factorial of  3 is 6
#--------------------------------------------------------
# Program to display Fibonacci series.
print("Program to display Fibonacci series.")
# Fibonacci series:  0, 1, 1, 2, 3, 5, 8, 13.....
def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def display_fibonacci_series(n):
    if n <= 0:
        print("Invalid input. Please enter a positive integer.")
    else:
        print("Fibonacci Series:") # Fibonacci Series:
        for i in range(1, n + 1):
            print(fibonacci(i), end=" ") # 0 1 1 2 3

num_terms = int(input("Enter the number of terms for Fibonacci series: "))
# Enter the number of terms for Fibonacci series: 5
display_fibonacci_series(num_terms)
''' Output:
    Enter the number of terms for Fibonacci series: 10
    Fibonacci Series:      
    0 1 1 2 3 5 8 13 21 34 
'''
#--------------------------------------------------------
#--------------------------------------------------------


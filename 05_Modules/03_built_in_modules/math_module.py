# math module
'''
Some functions in math module are
1. sqrt(x)
2. ceil(x)
3. floor(x)
4. fabs(x)
5. log(x)
6. sin(x)
7. tan(x)....etc'''
#--------------------------------------------------------
import math
#--------------------------------------------------------
print("-----sqrt(x)-----")
# Return the square root of x.
print(math.sqrt(45)) # 6.708203932499369
#--------------------------------------------------------
print("-----pow(x, y)-----")
# Return x**y (x to the power of y).
print(math.pow(2,3)) # 8.0
#--------------------------------------------------------
print("-----ceil(x)----")
# Return the ceiling of x as an Integral. This is the smallest integer >= x.
print(math.ceil(23.59)) # 24 
print(math.ceil(23.01)) # 24 
#--------------------------------------------------------
print("-----floor(x)-----")
# Return the floor of x as an Integral. This is the largest integer <= x.
print(math.floor(23.99)) # 23 
#--------------------------------------------------------
print("-----fabs(x)-----")
# Return the absolute value of the float x. # fabs(-x) = |x| 
print(math.fabs(-23.25)) # 23.25
print(math.fabs(-23)) # 23.0 
print(math.fabs(5)) # 5.0
#--------------------------------------------------------
print("-----isqrt(x)-----")
# Return the integer part of the square root of the input.
print(math.isqrt(45)) # 6
#--------------------------------------------------------
print("-----remainder(x, y)-----")
# Return the remainder.
print(math.remainder(10,3)) # 1.0
print(math.remainder(50,3)) # 1.0
#--------------------------------------------------------
print("-----modf(x)-----")
# Return the fractional and integer parts of x.
print(math.modf(12.23)) # (0.23000000000000043, 12.0)

#--------------------------------------------------------
#--------------------------------------------------------


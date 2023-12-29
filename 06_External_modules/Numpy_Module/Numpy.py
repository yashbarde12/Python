# Numpy Module
#--------------------------------------------------------
import numpy as np
#--------------------------------------------------------
# ndarray (n-dimensional array)
'''
- Ndarray is the n-dimensional array object defined in the numpy.
- it stores the collection of the similar type of elements.
'''
#--------------------------------------------------------
# Array function
print("-----numpy.array-----")
a = np.array
print(a) # <built-in function array>
#--------------------------------------------------------
# Creating numpy array (One Dimensional)
print("-----Creating 1D Array-----")
a = [1,2,3,4,5]
myarr = np.array(a)
print(myarr) # [1 2 3 4 5]

b = np.array([1,2,3])
print(b) # [1 2 3]   
print(type(b)) # <class 'numpy.ndarray'>
#--------------------------------------------------------
# Creating numpy array (Two Dimensional)
print("-----Creating 2D Array-----")
arr = np.array([[1,2,3],[4,5,6]])
print(arr) 
'''[[1 2 3]
    [4 5 6]] ''' 
print(type(arr)) # <class 'numpy.ndarray'>
#--------------------------------------------------------
# Dimension of the array
arr = np.array([[1,2,3],[4,5,6]])
print(arr.ndim)        
#--------------------------------------------------------
# Size of each item in an array in bytes
arr = np.array([[1,2,3],[4,5,6]])
print("Size of each item = ", arr.itemsize)    
#--------------------------------------------------------
# Size of the array
arr = np.array([[1,2,3],[4,5,6]])
print("Size of the array = ", arr.size)       
#--------------------------------------------------------
# Data type of elements in an array
arr = np.array([[1,2,3],[4,5,6]])
print("Data type of the array:", arr.dtype)
#--------------------------------------------------------
# No of rows and no of columns
arr = np.array([[1,2,3],[4,5,6]])
print("Shape of the array", arr.shape)         
#--------------------------------------------------------
# Changing the no of rows and columns
arr = np.array([[1,2,3],[4,5,6]])
arr = arr.reshape(3,2)                         
print("Array after reshaping")
print(arr)

arr = arr.reshape(1,6)
print("Array after reshaping")
print(arr)
#--------------------------------------------------------
# slicing
a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

print("Array :\n",a)
# 1. Get the element of specified location
print("Printing the element at 1st row and 2nd column\n",a[1,2])

# 2. Get the elements of specific index from each row 
print("Printing the elements of index 1 or column 1 from each row\n", a[0:,1])

print("Printing the elements of index 1 or column 1 from each 1st 3 rows\n", a[0:3,1])
#--------------------------------------------------------
# linspace() - To print evenly spaced values in a given interval
ln = np.linspace(1,5,10)
print(ln)
#--------------------------------------------------------
# Finding the max element from the array
a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print("Max element: ",a.max())
#--------------------------------------------------------
# Finding the min element from the array
a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print("Min element: ", a.min())
#--------------------------------------------------------
# Finding the sum of the array elements
a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print("Sum of all elements: ",a.sum())
#--------------------------------------------------------
# Numpy Axis
''' 
- Axis 0 represents the columns and 
- axis 1 represents the rows '''
a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

print("Sum of all elements in each column :",a.sum(axis = 0))

print("max element in each row:", a.max(axis = 1))

print("min element in each column:", a.min(axis = 0))
#--------------------------------------------------------
# Square root of elements
b = np.array([[1,4,9],[16,25,36]])
print("Square root of all elements:\n", np.sqrt(b))
#--------------------------------------------------------
# Standard deviation
''' Standard deviation means how much each element of the array 
    varies from the mean value of the numpy array '''
b = np.array([[1,4,9],[16,25,36]])

print("Standard deviation between elements", np.std(b))

print("Standard deviation between elements", np.std(a))
#--------------------------------------------------------
# Mathematical operations
c = np.array([[1,2,3],[4,5,6]])
d = np.array([[7,8,9],[10,11,12]])

print("Array c: \n",c)
print("Array d: \n",d)

print("Sum of the array c and d: \n", c+d)

print("Product of the array c and d: \n", c*d)

print("division of the array c and d: \n", c/d)
#--------------------------------------------------------
# Array Concatenation
c = np.array([[1,2,3],[4,5,6]])
d = np.array([[7,8,9],[10,11,12]])

print("Vertical concatenation:\n", np.vstack((c,d)))

print("Horizontal concatenation:\n", np.hstack((c,d)))
#--------------------------------------------------------
#--------------------------------------------------------

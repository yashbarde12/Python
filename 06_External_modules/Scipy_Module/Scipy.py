# Scipy Module
# Only uncomment (""" """)each section before executing for understanding.
#--------------------------------------------------------
# Scipy FFTpack module
'''
Fast fourier Transform is calulated by fft() function
Inverse transform is calculated by ifft() function '''
"""
# Example 1:
from scipy.fftpack import fft
import numpy as np
x = np.array([1,2,3,4])
y = fft(x)
print("Fast Fourier transform :",y)
"""
#--------------------------------------------------------
"""
# Example 2:
from scipy.fftpack import ifft
import numpy as np
x = np.array([1,2,3,4])
y = ifft(x)
print("Inverse FFT :",y)
"""
#--------------------------------------------------------
# Scipy Linear Algebra
# Solve Linear Equation
'''
Linear algebra problem can be solved by typing
linalg.solve() '''
#--------------------------------------------------------
# Example:
"""
''' Solve the linear equation a*x + b*y = z for following
    x + 3y + 10z = 10
    2x + 12y + 7z = 18
    5x + 8y + 8z = 30   '''

from scipy import linalg
import numpy as np
a = np.array([[1,3,10],[2,12,7],[5,8,8,]])
b = np.array([[10],[18],[30]])
x = linalg.solve(a,b)
print("Printing result:\n", x)
"""
#--------------------------------------------------------
# Find Determinant of Sqaure Matrix:
"""
from scipy import linalg
import numpy as np
mat = np.array([[5,9],[8,4]])
d= linalg.det(mat)
print("Determinant of matrix mat:\n", d)
"""
#--------------------------------------------------------
# Find Eigenvalues and Eigenvectors
"""
from scipy import linalg
import numpy as np
m1 = np.array([[3,2],[4,6]])
e_val, e_vec = linalg.eig(m1)
print("Printing Eigen Values:\n", e_val)
print("Printing Eigen Vectors:\n", e_vec)
"""
#--------------------------------------------------------
# Scipy Constant
# Various physical, mathematical constants and units used in scientific field

# Example:
"""
from scipy.constants import pi  
from math import pi  
#Comparing these two pi value  
print("sciPy - pi Value = %.18f" %pi)  
print("math - pi Value = %.18f" %pi)
"""
#--------------------------------------------------------
# Scipy Interpolation
# Interpolation means estimating intermediate value between the precise data points

# Example
"""
from scipy import interpolate
import matplotlib.pyplot as plt
x = np.arange(1,8)
y = np.exp(x)
print(y)
i = interpolate.interp1d(x,y)
x1 = np.arange(2,6)
y1 = i(x1)
plt.plot(x, y, 'o', x1, y1, '--')
plt.show()
"""
#--------------------------------------------------------
#--------------------------------------------------------

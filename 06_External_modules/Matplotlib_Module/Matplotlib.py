# Matplotlib Module
# Only uncomment (""" """)each section before executing for understanding.
#--------------------------------------------------------
# Example 1: Draw a line from position (1,4) to (2,5) then to (3,1)
"""
# plot() function : to draw a line from point to point
''' 
       Syntax - plot(parameter1, paramter2)
       parameter1 - an array containing x-axis points
       parameter2 - an array containing y-axis points  '''

from matplotlib import pyplot as plt
plt.plot([1,2,3],[4,5,1])
plt.show()
"""
#--------------------------------------------------------
# Example 2: Draw a line from from (1,1)  to (8,3)
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,8])
y = np.array([1,3])

plt.plot(x,y)
plt.show()
"""
#--------------------------------------------------------
# Example 3: Using Marker, linestype, color, linewidth
"""
import matplotlib.pyplot as plt
plt.plot([1,2,3],[4,5,1], marker = 'o', ls = '--', color = 'red', lw = 4)
plt.show()
"""
#--------------------------------------------------------
# Example 4: Draw two lines
"""
import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([1,3,5,7])
y1 = np.array([2,5,3,8])

y2 = np.array([5,1,8,3])

plt.plot(x1,y1, color = 'green')
plt.plot(y2)
plt.show() 
"""
#--------------------------------------------------------
# Example 5: Add title and x y label
"""
import matplotlib.pyplot as plt
import numpy as np

year = np.array([2016,2017,2018,2019,2020])
students_pass = np.array([50,48,47,51,53])
plt.title("Yearwise Student Result")
plt.subplot(1,3,1)
plt.plot(year,students_pass,marker = 'o', ls = '-.', color = 'green')

plt.xlabel("Year")
plt.ylabel("No of Students passed")

plt.grid()

plt.subplot(132)

plt.bar(year,students_pass)

plt.subplot(133)
plt.scatter(year,students_pass)
plt.show()
"""
#--------------------------------------------------------
# Bar Graph
# Vertical Bar graph
"""
from matplotlib import pyplot as plt  
players = ['Virat','Rohit','Shikhar','Hardik']  
runs = [51,87,45,67]  
plt.bar(players,runs,color = 'green')  
plt.title('Score Card')  
plt.xlabel('Players')  
plt.ylabel('Runs')  
plt.show()
"""
#--------------------------------------------------------
# Horizontal Bar Graph
"""
from matplotlib import pyplot as plt  
players = ['Virat','Rohit','Shikhar','Hardik']  
runs = [51,87,45,67]  
plt.barh(players,runs, color = 'green')  
plt.title('Score Card')  
plt.xlabel('Runs')  
plt.ylabel('Players')  
plt.show()
"""
#--------------------------------------------------------
# Style function in bar graph
"""
from matplotlib import pyplot as plt  
from matplotlib import style  
  
style.use('ggplot')  
  
x = [5,8,10]  
y = [12,16,6]  
  
x2 = [6,9,11]  
y2 = [7,15,7]

plt.bar(x, y, color = 'y', align='center')  
plt.bar(x2, y2, color='c', align='center')  
  
plt.title('Information')  
  
plt.ylabel('Y axis')  
plt.xlabel('X axis')

plt.show()
"""
#--------------------------------------------------------
# Pie Chart - Example 1
"""
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show()
"""
#--------------------------------------------------------
# Example 2:
"""
from matplotlib import pyplot as plt  
  
# Pie chart, where the slices will be ordered and plotted counter-clockwise:  
Players = 'Rohit', 'Virat', 'Shikhar', 'Yuvraj'  
Runs = [45, 30, 15, 10]  
explode = (0.1, 0, 0, 0)  # it "explode" the 1st slice   
    
plt.pie(Runs, explode=explode, labels=Players, shadow=True, startangle=90)   
  
plt.show()  
"""
#--------------------------------------------------------
# Histogram: Frequency Distribution graph
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

print(x)
plt.hist(x)
plt.show()
"""
#--------------------------------------------------------
# Example
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show()
"""
#--------------------------------------------------------
#--------------------------------------------------------

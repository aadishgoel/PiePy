# Calculation Of Pie :AAG
## Tribute For Pie Day 14th March 
### Yeah Monte Carlo Algo For Approximating Area 

from random import random,_pi
import matplotlib.pyplot as plt 

center = radius = 0.5

def check_inside(x,y):
    d = ((x-center)**2 + (y-center)**2)**0.5
    return d<=radius

simulation = 1000000
inside = outside = 0

n_points,pie_points,error_points=[],[],[]

print('*** Simulation Started ***')
for i in range(1,simulation+1):
    x,y = random(), random()
    if check_inside(x,y): inside +=1
    #### For Viz ####
    n_points.append(i)
    pie_points.append((inside/i)*4)
    error_points.append(abs(_pi-(inside/i)*4)/_pi *100)
    ### ###
print('*** Simulation Finished ***')

pie = (inside/simulation)*4
print('Value of Pie:',pie)
print('Error is:', abs(_pi-pie)/_pi *100 )

## All About Visualization
plt.title('pi.py Approxing pie with Monte Carlo Simulation')
plt.xlabel('Number Of Simulations')
plt.ylabel('Calculated Pie')
p1 = plt.plot(n_points, pie_points)
p2 = plt.axhline(y=_pi, color='r', linestyle='--')
plt.legend((p1[0], p2),('Calculated Pie', 'Actual Pie'))
plt.show()

plt.title('pi.py Error Values Over Time')
plt.xlabel('Number Of Simulations')
plt.ylabel('Percantage Error')
p1 = plt.plot(n_points, error_points)
p2 = plt.axhline(y=0, color='r', linestyle='--')
plt.legend((p1[0], p2),('Percentage Error', 'Zero Line'))
plt.show()

''' Output
*** Simulation Started ***
*** Simulation Finished ***
Value of Pie: 3.141964
Error is: 0.011820323356777651
'''

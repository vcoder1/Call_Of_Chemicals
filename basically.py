import time 
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import random
def illumination(x):
    a=1
    b=0
    return a*x+b

def isA(i, j):
    return grid[i][j]>=18 and grid[i][j]<19

def isB(i, j):
    return grid[i][j]>=19 and grid[i][j]<20

#n=10
n = int(input("Enter the size of the grid dipshit "))
brightEnoughColumn = int(51*n/100)
print(brightEnoughColumn)

k = 1
dt = 0.1 # dt babua


grid = np.random.rand(n, n) * 20
cmap = colors.ListedColormap(['white', 'blue', 'green'])
bounds = [0,18,19,20]
norm = colors.BoundaryNorm(bounds, cmap.N)

plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot()
fig.canvas.draw()
fig.canvas.flush_events()
time.sleep(1)
ax.imshow(grid, cmap=cmap, norm=norm)
fig.canvas.draw()
fig.canvas.flush_events()
fig.canvas.draw()
fig.canvas.flush_events()
time.sleep(1)

id_A=[] # son's idea of adding the positions in a list
       # you see,  ma boi's smort
       # yo ma boi
id_B=[] # not son's idea

temp=0

for i in range(n):
    for j in range(n):
        if(isA(i, j)):
            id_A.append([i, j, 0.01])
        if(isB(i, j)):
            id_B.append([i, j, 0.01])

for t in range(n):
    for r in range(len(id_A)):
        i, j, x = id_A[r]
        if j!=n-1 and j>=brightEnoughColumn:
            """First update positions of the bacterium"""
            temp = grid[i][j]
            grid[i][j] = grid[i][j+1]
            grid[i][j+1] = temp
            id_A[r][1] = id_A[r][1]+1

            """Update x"""
            dx = k*x*dt
            x = x+dx
            id_A[r][2] = x

    for r in range(len(id_B)):
        i, j, y = id_B[r]
        if isNearbyA(i, j):
            y=y+dy
            
                

    ax.imshow(grid, cmap=cmap, norm=norm)
    fig.canvas.draw()
    fig.canvas.flush_events()
    if n<=50:
        time.sleep(10/n)

    print(t)

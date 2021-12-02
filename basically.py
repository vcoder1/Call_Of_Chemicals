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

def isF(i, j):
    return grid[i][j]>=17 and grid[i][j]<18

#def isNearbyA(x, y):
#    # algorithm for detecting nearby A
#    t=2
#    if y+3<n:
#        for i in range(x-t, x+t+1):
#            for j in range(y-t, y+t):
#                #if isA(i, j) and j>=brightEnoughColumn:
#                if isA(i, j):
#                    return True
#
#        return False

Y1=[]
V1=[]
T=[]

th5 = 1

decayerOfY = 8.0/9 # the death of Y is imminent

V = [] # smort'nt

Y=[] # stores amt of 'y' in each cell(or compartment as son calls it)
c=10 # that constant in line #94
th2 = 1

th4 = 0
dy = 1

#n=10
n = int(input("Enter the size of the grid dipshit "))
brightEnoughColumn = int(51*n/100)
print(brightEnoughColumn)

k = 10
dt = 0.1 # dt babua


grid = np.random.rand(n, n) * 20
cmap = colors.ListedColormap(['white', 'yellow', 'blue', 'green'])
bounds = [0,17,18,19,20]
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

# initializing the id_A and id_B arrays
for i in range(n):
    for j in range(n):
        if(isA(i, j)):
            id_A.append([i, j, 0.0, 0.0])
        if(isB(i, j)):
            id_B.append([i, j, 0.0, 0.0])

# create a grid of zeros for Y
for i in range(n):
    Y.append([])
    for j in range(n):
        Y[i].append(0)

# create a grid of zeros for V
for i in range(n):
    V.append([])
    for j in range(n):
        V[i].append(0)

# meta updation loop - where each frame is being generated
for t in range(n):
    # updation for As
    for r in range(len(id_A)):
        i, j, X, v = id_A[r]
        v+=V[i][j]
        # update position of A's bacterium
        if j!=n-1 and j>=brightEnoughColumn:
            """First update positions of the bacterium"""
            temp = grid[i][j]
            grid[i][j] = grid[i][j+1]
            grid[i][j+1] = temp
            id_A[r][1] = id_A[r][1]+1

            """Update x"""
            dx = k*X*dt
            X = X+dx
            if v>th5:
                X=0
            id_A[r][2] = X
            


        # update the concentrations for Y in the entire grid
        for i1 in range(n):
            for j1 in range(n):
                if i1==i and j1==j:
                    continue
                if X > th2:
                    x = i1-i
                    y = j1-j
                    Y[i1][j1]+=1.0/(x*x+y*y) * c

                Y[i1][j1]/=decayerOfY


    # updation for Bs
    for r in range(len(id_B)):
        i, j, y, f= id_B[r]
        y+=Y[i][j]

        if isF(i, j-1):
            f+=1

        # update position of B's bacterium

        if j!=n-1 :
            if j>=1 and y>=th4:
                print("threshold reached; y = ", id_B[r][2])
                temp = grid[i][j]
                grid[i][j] = grid[i][j-1]
                grid[i][j-1] = temp
                id_B[r][1] = id_B[r][1]-1


            y-=Y[i][j]*0.9
            Y[i][j]=0
            id_B[r][2]=y

        # update the concentrations for V in the entire grid
        for i1 in range(n):
            for j1 in range(n):
                if i1==i and j1==j:
                    continue

                x = i1-i
                y = j1-j
                V[i1][j1]+=1.0/(x*x+y*y) * f
                                   

    ax.imshow(grid, cmap=cmap, norm=norm)
    fig.canvas.draw()
    fig.canvas.flush_events()
    if n<=50:
        time.sleep(1/n)

    print(t)

    sumV = 0
    sumY = 0
    for i in range(n):
        for j in range(n):
            sumV += V[i][j]
            sumY += Y[i][j]

    V1.append(sumV)
    Y1.append(sumY)
    T.append(t)
print(Y1)
print(T)
print(V)

import matplotlib.pyplot as plt1
#plt.plot(V1, T)
plt1.plot(Y1, T)
plt1.show()

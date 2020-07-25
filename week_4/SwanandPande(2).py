import random
import numpy as np
import pandas as pd
import math
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt

a=np.zeros(shape=(100,150))
a[50][75]=1
count=[]
change=[0]
iteration=0
X=[0]
while (np.count_nonzero(a==1) != 15000):

    for i in range(8):
        k=random.randint(0, 99)
        b=random.randint(0,149)
        c=random.randint(0, 99)
        d=random.randint(0,149)
        temp = a[k][b]
        a[k][b]=a[c][d]
        a[c][d]=temp
    count.append(np.count_nonzero(a == 1))
    for i in range(100):
        for j in range(150):
            if a[i][j]==1 :
                for r in range(j-1 , j+2):
                    if(r!=-1 and r!=150):
                        if(r!=j):
                            if random.uniform(0,1)<= 0.25 :
                                a[i][r]= 1;
                        if i-1 != -1:
                            if random.uniform(0, 1) <= 0.25:
                                a[i-1][r] = 1;
                        if i + 1 != 100:
                            if random.uniform(0, 1) <= 0.25:
                                a[i + 1][r] = 1;
                for r in range(j-2, j+3):
                    if (r > -1 and r < 150):
                        if (r != j and r!=j-1 and r!=j+1):
                            if random.uniform(0, 1) <= 0.08:
                                a[i][r] = 1;
                        if i - 2 > -1:
                            if random.uniform(0, 1) <= 0.08:
                                a[i - 2][r] = 1;
                        if i + 2 < 100:
                            if random.uniform(0, 1) <= 0.08:
                                a[i + 2][r] = 1;
    iteration+=1
    X.append(iteration)
    change.append(np.count_nonzero(a==1)-count[iteration-1] )
count.append(15000)

plt.bar(X,count)
plt.xlabel('Number of Iterations')
plt.ylabel('Number of Ones present')
plt.show()
ymax = max(change)
xpos = change.index(ymax)
xmax = X[xpos]
print(xmax,ymax)
plt.bar(X,change)
plt.xlabel('Number of Iterations')
plt.ylabel('Change in number of Ones ')

plt.show()


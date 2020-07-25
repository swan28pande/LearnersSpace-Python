import random
import numpy as np
import pandas as pd
import math
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt

List = []
#added a comment
for i in range(1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice3 = random.randint(1, 6)
    sum = dice1+dice2+dice3
    List.append(sum)
a= np.array(List,dtype=int)
List2=[]
List3=[]
for i in range(3,19):
    List2.append(i)
    List3.append((List.count(i))/1000)
X=List2
y=List3
yhat = savgol_filter(y, 15, 12)
plt.bar(X,y)
plt.title('Probablity Vs Sum of outcomes of 3 dices')
plt.xlabel('Sum of outcomes of 3 dices')
plt.ylabel('Probablity')
plt.plot(X,yhat,color = 'red')
plt.show()

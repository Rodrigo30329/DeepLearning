# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 18:15:25 2022

@author: juanc
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
plt.close()
#x1=np.array([1,   1,  2, 3, 5, 2])
#x2=np.array([1,   2,  1, 3, 2, 5])
#Yd=np.array([-5, -3, -2, 5, 9, 6])

#x1=np.array([0.1, -0.3, 0.5, 1.0, 1.2, 0.1, 0.9, -0.2, 0.8 , 1.3])
#x2=np.array([0.1,   0.1, 1.2, 0.6, 0.8, 0.3, 1.2, 0.3,  0.9,  1.5])
#Yd=np.array([0,     0,    1,   1,    1,  0,   1,     0,    1,   1  ])

df=pd.read_excel(r'Datos12022DL.xlsx',sheet_name='Sheet7')
dfa=df.values
X=dfa[:,0]
Yd=dfa[:,3]
plt.figure(1)
plt.plot(X,Yd,'*b')
#plt.plot(X[30:40,0],X[30:40,1],'*r',X[0:10,0],X[0:10,1],'*r')

alfa=0.01
W0=np.random.randn(1)
W1=np.random.randn(1)
#W2=np.random.randn(1)
epocas=3000
E2=np.zeros(epocas)
for epoca in range(0,epocas):
    p=np.random.permutation(len(X))
    for i in range(0,len(X)):
        #Ynet=X[p[i],0]*W1+X[p[i],1]*W2+W0
        Ynet=X[p[i]]*W1+W0
        Y=Ynet
        # Funcion de activacion
        #if (Ynet<0):
        #    Y=0
        #else: Y=1              
        
        error=(Yd[p[i]]-Y)
        #W2=W2+alfa*error*X[p[i],1]
        W1=W1+alfa*error*X[p[i]]
        W0=W0+alfa*error*1
        
    #Ye=W1*X[:,0]+W2*X[:,1]+W0
    Ye=W1*X[:]+W0
    #Ye=np.heaviside(Ye,1)
    
    E2[epoca]=np.sum((Yd-Ye)**2)/2

plt.plot(X,Ye,'r')

"""
X2r1_5=(-W0-1.5*W1)/W2

X2r_0_2=(-W0+0.2*W1)/W2

plt.plot([1.5, -0.2], [X2r1_5, X2r_0_2])
"""
print(E2)
plt.figure(2)
plt.plot(E2)
plt.grid()

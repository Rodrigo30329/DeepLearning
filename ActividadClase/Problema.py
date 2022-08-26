
import numpy as np
import matplotlib.pyplot as plt

X1 = np.array([1, 1, 2, 3, 5, 2])
X2 = np.array([1, 2, 1, 3, 2, 5])
Yd = np.array([-5, -3, -2, 5, 9, 6])

Alfa = 0.01
W0 = np.random.randn(1)
W1 = np.random.randn(1)
W2 = np.random.randn(1)
Epocas = 30
E2=np.zeros(Epocas)

for epoca in range(Epocas):
    p = np.random.permutation(len(X1))  
    for i in range(len(X1)):
        Ynet = X1[(p[i])]*W1+X2[p[i]]*W2+W0
        #función de activación
        Y = Ynet
        #cáculo error
        Error = (Yd[p[i]]-Y)
        W1 = W1+Alfa*Error*X2[p[i]]
        W2 = W2+Alfa*Error*X2[p[i]]
        W0 = W0+Alfa*Error*1        
    Ye = W1*X1+W2*X2+W0
    E2 = np.sum((Yd-Ye)**2)/2
    print(epoca, E2)
print(E2)
plt.figure(1)
plt.plot(E2)
plt.show()
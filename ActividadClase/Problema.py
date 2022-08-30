
import numpy as np
import matplotlib.pyplot as plt

# X1 = np.array([1, 1, 2, 3, 5, 2])
# X2 = np.array([1, 2, 1, 3, 2, 5])
# Yd = np.array([-5, -3, -2, 5, 9, 6])


X1 = np.array([0.1, -0.3, 0.5, 1.0, 1.2, 0.1, 0.9, -0.2, 0.8, 1.3])
X2 = np.array([0.1, 0.1, 1.2, 0.6, 0.8, 0.3, 1.2, 0.3, 0.9, 1.5])
Yd = np.array([0, 0, 1, 1, 1, 0, 1, 0, 1, 1])

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
        if Ynet<0:
            Y=0
        else:
            Y=1
        #cáculo error
        Error = (Yd[p[i]]-Y)
        W1 = W1+Alfa*Error*X2[p[i]]
        W2 = W2+Alfa*Error*X2[p[i]]
        W0 = W0+Alfa*Error*1        
    Ye = W1*X1+W2*X2+W0
    Ye = np.heaviside(Ye,1)
    E2 = np.sum((Yd-Ye)**2)/2
    print(epoca, E2)
print(E2)
plt.figure(1)
plt.plot(E2)
<<<<<<< HEAD
plt.grid()
=======
plt.show()
>>>>>>> f00cf825148495c19b97c3360c60d0c371eca631

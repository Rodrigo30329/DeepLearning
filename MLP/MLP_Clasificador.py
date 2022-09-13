import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split

df=pd.read_excel('Datos12022DL.xlsx', 'Sheet5')
dfa=df.values
x=dfa[:,0:2]
y=dfa[:,2]

plt.figure(1)
for i in range(0, len(y)):
    if y[i] == 0:
        plt.plot(x[i,0],x[i,1],'or')
    else:
        plt.plot(x[i,0],x[i,1],'og')

plt.show(1)

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.1, random_state=0)

MLP_Clas = Sequential()
MLP_Clas.add(Dense(output_dim=6, init='uniform', activation='relu', input_dim=2))
MLP_Clas.add(Dense(output_dim=6, init='uniform', activation='relu'))
MLP_Clas.add(Dense(output_dim=1, init='uniform', activation='sigmoid'))

MLP_Clas.compile('adam', loss='binary_crossentropy', metrics=['accuracy'])

history=MLP_Clas.fit(x_train, y_train, batch_size=20, nb_epoch=600)

Yt=MLP_Clas.predict(x_test)
Yt_01=np.heaviside(Yt-0.5,1)
print("Salida= ", Yt_01. T)
print("deseado= ", y_test.T)

plt.figure(1)
plt.plot(history.history['loss'])
plt.grid()

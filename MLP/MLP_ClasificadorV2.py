import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

df=pd.read_excel('Datos1_2022DL.xlsx', 'Sheet5')
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
MLP_Clas.add(Dense(units=3, kernel_initializer='uniform', activation='relu', input_dim=2))
MLP_Clas.add(Dense(units=2, kernel_initializer='uniform', activation='relu'))
MLP_Clas.add(Dense(units=1, kernel_initializer='uniform', activation='sigmoid'))

MLP_Clas.compile('adam', loss='binary_crossentropy', metrics=['accuracy'])

history=MLP_Clas.fit(x_train, y_train, batch_size=20, epochs=200)

Yt=MLP_Clas.predict(x_test)
Yt_01=np.heaviside(Yt-0.5,1)

Ytrain=MLP_Clas.predict(x_train)
Ytrain_01=np.heaviside(Yt-0.5,1)

plt.figure(1)
plt.plot(history.history['loss'])
plt.grid()

MCTest=confusion_matrix(y_test, Yt_01)
MCTrain=confusion_matrix(y_train, Ytrain_01)
print(MCTest)
print(MCTrain)

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split

df=pd.read_excel('Datos1_2022DL.xlsx', 'Sheet4')
dfa=df.values
x=dfa[:,0]
y=dfa[:,1]

plt.figure(1)
plt.plot(x,y,'or')
plt.show()

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.1, random_state=0)

MLP_Reg = Sequential()
MLP_Reg.add(Dense(units=6, kernel_initializer='uniform', activation='relu', input_dim=1))
MLP_Reg.add(Dense(units=6, kernel_initializer='uniform', activation='relu'))
MLP_Reg.add(Dense(units=1, kernel_initializer='uniform')

MLP_Reg.compile('adam', loss='mean_squared_error', metrics=['accuracy'])

history=MLP_Reg.fit(x_train, y_train, batch_size=10, epochs=1000)

Y=MLP_Reg.predict(x)

plt.figure()
plt.plot(x,Y[:,0],'ob')
plt.grid()

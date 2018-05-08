# Variable

from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import Embedding
from keras.layers import LSTM
import numpy as np

model = Sequential()
model.add(Dense(1000, input_dim=50, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

X = []
y = []

for i in range(100000):
    x_hold = []
    value = np.random.randint(2, size=np.random.randint(1, 50))
    for x in value:
        x_hold.append(int(x))
    if sum(x_hold) % 2 == 1:
        y.append(1)
    else:
        y.append(0)
    X.append(x_hold)
X = np.array(X)
y = np.array(y)

x_train, x_test = X[:90000], X[90000:]
y_train, y_test = y[:90000], y[90000:]

model.fit(x_train, y_train, batch_size=10000, epochs=10)
score = model.evaluate(x_test, y_test, batch_size=4)


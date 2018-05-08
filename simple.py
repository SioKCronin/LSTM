from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import Embedding
from keras.layers import LSTM
import numpy as np

model = Sequential()
model.add(Dense(10, input_dim=5, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

X = []
y = []

for i in range(10):
    x_hold = []
    value = np.random.randint(2, size=5)
    for x in value:
        x_hold.append(int(x))
    if sum(x_hold) % 2 == 1:
        y.append(1)
    else:
        y.append(0)
    X.append(x_hold)
X = np.array(X)
y = np.array(y)

x_train, x_test = X[:8], X[8:]
y_train, y_test = y[:8], y[8:]

model.fit(x_train, y_train, batch_size=16, epochs=10)
score = model.evaluate(x_test, y_test, batch_size=16)

#for i in range(n):
#    value = np.random.randint(2, size=np.random.randint(1, string_size))
#    for x in value:
#        fh.write(str(x))
#    if int(value[-1]) == 1:
#        fh.write(",1.0")
#    else:
#        fh.write(",0")
#    fh.write('\n')

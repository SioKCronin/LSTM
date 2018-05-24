from sklearn.model_selection import train_test_split
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import Embedding
from keras.layers import LSTM
import numpy as np
import pandas as pd

def generate_data(test_split = 0.2, variable=False):
    print("---Generating Data---")

    X = []
    y = []

    for i in range(10000):
        x_hold = []

        if variable:
            value = np.random.randint(2, size=np.random.randint(1, 50))
        else:
            value = np.random.randint(2, size=50)

        for x in value:
            x_hold.append(int(x))
        if sum(x_hold) % 2 == 1:
            y.append(0)
        else:
            y.append(1)
        X.append(x_hold)

    X = np.array(X)
    y = np.array(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    y_train = pd.get_dummies(y_train).values
    y_test = pd.get_dummies(y_test).values

    return X_train, y_train, X_test, y_test

def create_LSTM_model(input_length):
    print('---Creating LSTM model---')
    embed_dim = 128
    lstm_out = 200

    model = Sequential()
    model.add(Embedding(10000, embed_dim, input_length=50, dropout = 0.2))
    model.add(LSTM(lstm_out, dropout_U = 0.2, dropout_W = 0.2))
    model.add(Dense(2, activation='softmax'))
    model.compile(loss='mse',
                  optimizer='adam',
                  metrics=['accuracy'])
    print(model.summary())
    return model

X_train, y_train, X_test, y_test = generate_data()

model = create_LSTM_model(len(X_train[0]))
model.fit(X_train, y_train, batch_size=10, epochs=10)
model.evaluate(X_test, y_test, batch_size=4)

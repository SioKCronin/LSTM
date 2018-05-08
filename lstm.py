# Long Short-Term Memory

import tensorflow as tf
import collections
import numpy as np

input_file = 'data_50.csv'

def load_data(test_split = 0.2):
    print ('Loading data...')
    df = pd.read_csv(input_file)
    df['sequence'] = df['sequence'].astype(str)

def build_dataset(words):
    count = collections.Counter(words).most_common()
    dictionary = dict()
    for word, _ in count:
        dictionary[word] = len(dictionary)
    reverse_dictionary = dict(zip(dictionary.values(), dictionary.keys()))
    return dictionary, reverse_dictionary

def RNN(training_data, weights, biases):
    # reshape to [1, n_input]
    x = tf.reshape(x, [-1, n_input])

    # Generate a n_input-element sequence of inputs
    x = tf.split(x, n_input, 1)

    # 1-layer LSTM with n_hidden units
    rnn_cell = rnn.BasicLSTMCell(n_hidden)

    # generate prediction
    outputs, states = rnn.static_rnn(rnn_cell, x, dtype=tf.float32)

    # there are n_input outputs but we want the last output
    return tf.matmul(outputs[-1], weights['out']) + biases['out']

dictionary, reverse_dictionary = build_dataset(training_data)

vocab_size = len(dictionary)
n_input = 3
offset = 1

# number of units in RNN cell
n_hidden = 512

# RNN output node weights and biases
weights = {'out':tf.Variable(tf.random_normal([n_hidden, vocab_size]))}
biases = {'out': tf.Variable(tf.random_normal([vocab_size]))}

symbols_in_keys = [[dictionary[str(training_data[i])]] for i in range(offset, offset+n_input)]

symbols_out_onehot = np.zeros([vocab_size], dtype=float)
symbols_out_onehot[dictionary[str(training_data[offset+n_input])]]= 1.0

session = tf.Session()

# Define an optimizer - https://stats.stackexchange.com/questions/168513/what-optimization-methods-work-best-for-lstms

_, acc, loss, onehot_pred = session.run([optimizer, accuracy, cost, pred],
    feed_dict={x: symbols_in_keys, y: symbols_out_onehot})

pred = RNN(training_data, weights, biases)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred, labels=y))
optimizer = tf.train.RMSPropOptimizer(learning_rate=learning_rate).minimize(cost)

rnn_cell = rnn.MultiRNNCell([rnn.BasicLSTMCell(n_hidden), rnn.BasicLSTMCell(n_hidden)])

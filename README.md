# Grid LSTM

The goal of this repo is to implement and explore the implications of this paper, [Grid Long Short Term Memory](https://arxiv.org/pdf/1507.01526v3.pdf), inspired by OpenAI's [Request for Research 2.0](https://blog.openai.com/requests-for-research-2/). 

## The Problem

Train an LSTM to solve the XOR problem: that is, given a sequence of bits, determine its parity. The LSTM should consume the sequence, one bit at a time, and then output the correct answer at the sequence’s end. 

- [X] Generate a dataset of random 100,000 binary strings of length 50. Train the LSTM; what performance do you get?
* **With 10 epochs, I got 0.5025 accuracy.** 
* **I fiddled with dropout and epochs, and saw performance wasn't improving, so I hunted around for insight into what might be happening. Christopher Bourez's blog let me do to [this paper](https://arxiv.org/abs/1507.01526).**
- [X] Implement simple verbose LSTM (not with Keras).
- [ ] Create simple grid LSTM architecture. 
- [ ] Generate a dataset of random 100,000 binary strings, where the length of each string is independently and randomly chosen between 1 and 50. Train the LSTM. Does it succeed? What explains the difference?

## Resources

* [Reference - Tensorflow](https://github.com/phvu/grid-lstm-tensorflow/tree/master/char_rnn)
* [Reference - Keras](https://github.com/davidbuniat/GridLSTM)
* [LSTM parameters](https://stackoverflow.com/questions/45278286/how-to-choose-lstm-keras-parameters?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa)
* [Understanding LSTM](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)
* [Tensorflow RNN cells](https://github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/rnn/python/ops/rnn_cell.py)

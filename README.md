# 1D Grid LSTM Network

Implementation of the XOR problem with Long Short-Term Memory (LSTM), inspired by OpenAI's [Request for Research 2.0](https://blog.openai.com/requests-for-research-2/). 

## The Problem

Train an LSTM to solve the XOR problem: that is, given a sequence of bits, determine its parity. The LSTM should consume the sequence, one bit at a time, and then output the correct answer at the sequence’s end. 

- [X] Generate a dataset of random 100,000 binary strings of length 50. Train the LSTM; what performance do you get?
* **With 10 epochs, I got 0.5025 accuracy.** 
* **I fiddled with dropout and epochs, and saw performance wasn't improving, so I hunted around for what insight into what might be happening. Christopher Bourez's blog let me do to [this paper](https://arxiv.org/abs/1507.01526) which I've reviewed here.**
- [ ] Generate a dataset of random 100,000 binary strings, where the length of each string is independently and randomly chosen between 1 and 50. Train the LSTM. Does it succeed? What explains the difference?

## Resources

* [LSTM parameters](https://stackoverflow.com/questions/45278286/how-to-choose-lstm-keras-parameters?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa)
* [Understanding LSTM](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)
* [Another great tutorial](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)
* [Implementation example in Numpy](http://blog.varunajayasiri.com/numpy_lstm.html)
* [Implementation by Trask](https://iamtrask.github.io/2015/11/15/anyone-can-code-lstm/)
* [Another example](https://machinelearningmastery.com/binary-classification-tutorial-with-the-keras-deep-learning-library/)

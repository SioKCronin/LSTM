# LSTM_Network

Implementation of a Long Short-Term Memory network, inspired by OpenAI's [Request for Research 2.0](https://blog.openai.com/requests-for-research-2/). 

## OpenAI's motivating question

Train an LSTM to solve the XOR problem: that is, given a sequence of bits, determine its parity. The LSTM should consume the sequence, one bit at a time, and then output the correct answer at the sequence’s end. 

- [X] Generate a dataset of random 100,000 binary strings of length 50. 
- [ ] Train the LSTM; what performance do you get?
- [ ] Generate a dataset of random 100,000 binary strings, where the length of each string is independently and randomly chosen between 1 and 50. 
- [ ] Train the LSTM. Does it succeed? What explains the difference?

## Resources

* [Where I started](https://towardsdatascience.com/lstm-by-example-using-tensorflow-feb0c1968537)
* [Understanding LSTM](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)
* [Implementation example in Numpy](http://blog.varunajayasiri.com/numpy_lstm.html)
* [Implementation by Trask](https://iamtrask.github.io/2015/11/15/anyone-can-code-lstm/)

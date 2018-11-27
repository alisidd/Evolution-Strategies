I am attempting to implement the algorithm outlined in https://arxiv.org/pdf/1703.03864.pdf

The core of the algorithm will be implemented in `es.py`. The core of the algorithm runs multiple threads that adds a random seed to an array of weights. To test this function, I have simplified it so it adds `worker_id` to the array of weights instead of a random number, then I check to see if the result is what I expected.

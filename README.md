I am attempting to implement the algorithm outlined in https://arxiv.org/pdf/1703.03864.pdf

The core of the algorithm will be implemented in `es.py`, as the algorithm runs threads asynchronously that modify the weight in some way, I have written a simpler version of the function and test if it works for multiple threads  

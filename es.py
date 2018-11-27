import tensorflow as tf
import numpy as np

from multiprocessing.pool import ThreadPool

def worker_thread(weights, seed=None):
    new_weights = weights + seed
    return new_weights

def test_workers():
    n, workers = 3, []
    pool = ThreadPool(processes=3)
    weights = np.array([3,4,5])

    for i in range(n):
        workers.append(pool.apply_async(worker_thread, (weights, i)))

    for i, worker in enumerate(workers):
        assert((worker.get() == weights + i).all())

    print('Workers test passed')

if __name__ == '__main__':
    test_workers()

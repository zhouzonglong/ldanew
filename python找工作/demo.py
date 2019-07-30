import numpy as np

X = 1. / (np.arange(1, 11) + np.arange(0, 10)[:, np.newaxis])
# print(X)
print(np.arange(0, 10)[:, np.newaxis])
print(np.arange(1,11).reshape(10,1))
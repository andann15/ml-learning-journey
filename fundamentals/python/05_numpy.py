# 05_numpy.py
# Operasi numerik untuk Machine Learning

import numpy as np

# Array
data = np.array([10, 20, 30, 40])
print("Data:", data)

# Mean & Standard Deviation
print("Mean:", np.mean(data))
print("Std:", np.std(data))

# Matrix
weights = np.array([[0.2, 0.5], [0.3, 0.7]])
inputs = np.array([1, 0])

output = np.dot(weights, inputs)
print("Output neuron:", output)

import numpy as np

def sigmoid(x):
    return 1/(1 + np.exp(-x))

def relu(x):
    return max(0, x)

def tanh(x):
    (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

def leaky_relu(x):
    if x > 0 :
        return x
    if x <= 0:
        return 0.01 * x

print(leaky_relu(-1))
print(leaky_relu(-5))
print(leaky_relu(-10))

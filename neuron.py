import numpy as np

# Basic activation functions
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

#print(relu(-5))
#print(leaky_relu(-1))
#print(leaky_relu(-10))

# Basic 2 layer network.
def initialize_parameters_2_layers(n_input, n_hidden, n_output):
    np.random.seed(24)

    weights_1 = np.random.randn(n_hidden, n_input)
    bias_1 = np.zeros(n_hidden, 1)

    weights_2 = np.random.randn(n_hidden, n_output)
    bias_2 = np.zeros(n_output, 1)

    return weights_1, bias_1, weights_2, bias_2 

# Here is an example for how the matrices look.
'''
n_input = 3    # 3 input features
n_hidden = 5   # 5 hidden neurons
n_output = 2   # 2 output neurons (e.g. binary classification with softmax)

n_input = [ x1,
            x2,
            x3]

    shape = (3, 1)

n_hidden = [
    [ 00, 01, 02 ]
    [ 10, 11, 12 ]
    [ 30, 31, 32 ]
    [ 40, 41, 42 ]
    [ 50, 51, 52 ]]

    shape = (5, 3)

bias_1 = [0,
          0,
          0,
          0,
          0,
           ]
    
    shape = (5, 1)

Hidden layer linear transformation
Z1 = W1⋅X + b1 ⇒ (5,3)⋅(3,1)=(5,1)
Z1 = W1⋅X + b1 ⇒ (5,3)⋅(3,1)=(5,1)



weight_2 = [
    [0.2, -0.1, 0.05, -0.3, 0.1],
    [-0.2, 0.3, -0.05, 0.1, -0.4]
])  
    Shape = (2, 5)

bias_2 = [0,
          0
           ]
    shape = (2, 1)

Output layer transformation
Z2 = W2⋅A1 + b2 ⇒ (2,5)⋅(5,1)=(2,1)
Z2 = W2⋅A1 + b2 ⇒ (2,5)⋅(5,1)=(2,1)

n_output = [y0,
            y1 ]

'''

# neural-networks-scratch

🔁 Common Activation Functions
1. Sigmoid
 - sigmoid(z) = 1 / (1+e^(−z))

    Range: (0, 1)

    Used in: Output layer for binary classification

    Problem: Can cause vanishing gradients in deep networks

 - Visual: S-shaped curve
2. Tanh (Hyperbolic Tangent)
 - tanh(z) = (e^(z) − e^(−z)) / (e^(z) + e^(−z))

    Range: (-1, 1)

    Zero-centered (better than sigmoid in practice)

    Still suffers from vanishing gradients, but less than sigmoid

3. ReLU (Rectified Linear Unit)
 - ReLU(z) = max⁡(0,z)

    Range: [0, ∞)

    Very common in hidden layers

    Fast to compute

    Issue: “Dying ReLU” — neurons can get stuck and always output 0
   
Two Layer Network and Explanation

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

- Hidden layer linear transformation
   Z1 = W1⋅X + b1 ⇒ (5,3)⋅(3,1)=(5,1)

weight_2 = [
    [0.2, -0.1, 0.05, -0.3, 0.1],
    [-0.2, 0.3, -0.05, 0.1, -0.4]
]  
    Shape = (2, 5)

bias_2 = [0,
          0
           ]
    shape = (2, 1)

- Output layer transformation
   Z2 = W2⋅A1 + b2 ⇒ (2,5)⋅(5,1)=(2,1)

n_output = [y0,
            y1 ]

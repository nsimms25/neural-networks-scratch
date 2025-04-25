import sys
import numpy as np

print("I am alive")
print(sys.executable)

import numpy as np

# Testing my logic for input, mulitple hidden, and output layers.

# Number of nodes for input layer, hidden layers, and output layer
n_input = 3
n_hidden = [4, 5, 3]
n_output = 2

weight_matrix_list = []

# Input weights
input_weights = np.random.randn(n_input, n_hidden[0])
weight_matrix_list.append(input_weights)

# Hidden weights
for i in range(1, len(n_hidden)):
    weight_matrix = np.random.randn(n_hidden[i-1], n_hidden[i])  # Shape: (previous layer neurons, current layer neurons)
    weight_matrix_list.append(weight_matrix)

output_weights = np.random.randn(n_hidden[-1], n_output)
weight_matrix_list.append(output_weights)

# Example output
for i, weight_matrix in enumerate(weight_matrix_list):
    print(f"Weight matrix for layer {i+1}:")
    print(weight_matrix)
    print("\n")

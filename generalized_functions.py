"""
generalized_functions.py

This file is to create generalized functions for more flexible use. 

Date: 2025-04-24
Version: 0
"""

import numpy as np

def general_init_parameters(n_input: int, n_hidden: list[int], n_output, init_method = "he"):
    """
    General_init_parameters is to generalize the parameter initialization.
    This is for a fully connected list with at least one hidden layer.

    Args:
        n_input: number of inputs (int).
        n_hidden: number of neurons in hidden layer.
        n_output: number of output neurons.
        init_method: the additional method used in initialization.
    
    Returns:
        weight_list: list of weight matrices.
        bias_list: list of bias matrices.
    """
    np.random.seed(45)
    
    weight_matrix_list = []
    bias_matrix_list = []

    input_weights = np.random.randn(n_input, n_hidden[0])
    input_bias = np.random.randn(n_input, n_hidden[0])

    weight_matrix_list.append(input_weights)
    bias_matrix_list.append(input_bias)

    for i in range(1, len(n_hidden)):
        weight_matrix = np.random.randn(n_hidden[i-1], n_hidden[i])
        weight_matrix_list.append(weight_matrix)
        
        bias_matrix = np.random.randn(n_hidden[i-1], n_hidden[i])
        bias_matrix_list.append(bias_matrix)
    """
    What we should do is create the shape of the 
    currect weight and bias based on the index. 
    """
    output_weights = np.random.randn(n_hidden[-1], n_output)
    output_bias = np.random.randn(n_hidden[-1], n_output)

    weight_matrix_list.append(output_weights)
    bias_matrix_list.append(output_bias)

    return weight_matrix_list, bias_matrix_list
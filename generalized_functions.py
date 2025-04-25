"""
generalized_functions.py

This file is to create generalized functions for more flexible use. 

Author: Your Name
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

    holding_dict = {}

    for i, layer_num in enumerate(n_hidden):
        if i == 1:
            weight_0 = np.random.randn(n_input, n_hidden[layer_num]) #Always 1 hidden layer.
            weight_matrix_list.append(weight_0)
        else:
            holding_dict[f"layer{i}"] = np.random.randn(weight_matrix_list[i-1], n_hidden[layer_num]) #Always 1 hidden layer.
            weight_matrix_list.append(holding_dict[f"layer{1}"])

    




    return weight_matrix_list, bias_matrix_list
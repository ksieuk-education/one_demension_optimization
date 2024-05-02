import math


def euclidean_norm(vector):
    """
    Calculate the Euclidean norm of a vector.

    Parameters:
    vector (list): List of coordinates representing the vector

    Returns:
    norm (float): Euclidean norm of the vector
    """
    squared_sum = sum(xi**2 for xi in vector)
    return math.sqrt(squared_sum)

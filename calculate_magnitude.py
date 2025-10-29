import numpy as np

def calculate_magnitude(X):
    magnitude = np.abs(X) / len(X)
    magnitude = magnitude[:len(magnitude) // 2]
    magnitude[1 : -1] = 2 * magnitude[1 : -1]
    return magnitude
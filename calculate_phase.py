import numpy as np

def calculate_phase(X):
    phase = np.unwrap(np.angle(X))
    phase = phase[:len(phase) // 2]
    return phase
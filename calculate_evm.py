import numpy as np

def calculate_evm(reference_symbols, actual_symbols):
    error = actual_symbols - reference_symbols
    evm = np.sqrt(np.mean(np.abs(error) ** 2) / np.mean(np.abs(reference_symbols) ** 2)) * 100
    return evm
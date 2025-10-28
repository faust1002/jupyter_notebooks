import numpy as np

def resample_by_interpolation(signal, down, up):
    scale = up / down
    n = np.round(len(signal) * scale)

    resampled_signal = np.interp(np.linspace(0.0, 1.0, int(n), endpoint = False),
                                 np.linspace(0.0, 1.0, len(signal), endpoint = False),
                                 signal)
    return resampled_signal
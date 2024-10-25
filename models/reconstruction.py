import numpy as np
from models.signal import signal, signalType

class Reconstructor:
    def __init__(self, sampled_signal: signal):
        self.sampled_signal = sampled_signal

    def reconstruct(self, t: np.ndarray, sampling_frequency):
        x_vec = self.sampled_signal.x_vec
        y_vec = self.sampled_signal.y_vec

        # whittaker-shannon interpolation formula
        y_interp = np.zeros_like(t)
        for i, t_val in enumerate(t):
            y_interp[i] = np.sum(y_vec * np.sinc((x_vec - t_val) * sampling_frequency))
        
        return signal(np.array(t), np.array(y_interp), signalType.CONTINUOUS)

from models.signal import signal, signalType
import numpy as np

class Reconstructor:
    def __init__(self, sampled_signal: signal):
        self.sampled_signal = sampled_signal
    def reconstruct_whittaker_shannon(self, t: np.ndarray, sampling_frequency):
        x_vec = self.sampled_signal.x_vec
        y_vec = self.sampled_signal.y_vec

        # Whittaker-Shannon interpolation formula
        y_interp = np.zeros_like(t)
        for i, t_val in enumerate(t):
            y_interp[i] = np.sum(y_vec * np.sinc((x_vec - t_val) * sampling_frequency))
        
        return signal(np.array(t), np.array(y_interp), signalType.CONTINUOUS)
    
    def reconstruct_zero_order_hold(self, t: np.ndarray):
        x_vec = self.sampled_signal.x_vec
        y_vec = self.sampled_signal.y_vec

        # Zero-Order Hold (Step function interpolation)
        y_interp = np.interp(t, x_vec, y_vec, left=None, right=None)
        
        return signal(np.array(t), np.array(y_interp), signalType.CONTINUOUS)
    
    def reconstruct_nearest_neighbor(self, t: np.ndarray):
        
        x_vec = self.sampled_signal.x_vec
        y_vec = self.sampled_signal.y_vec
        y_interp = np.zeros_like(t)
        for i in range(len(t)):
            # Find the index of the nearest sampled value
            idx = np.argmin(np.abs(x_vec - t[i]))
            y_interp[i] = y_vec[idx]  # Assign the nearest sample value

        return signal(np.array(t), np.array(y_interp), signalType.CONTINUOUS)


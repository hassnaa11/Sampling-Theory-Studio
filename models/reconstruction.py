from models.signal import signal, signalType
from scipy.interpolate import CubicSpline
import numpy as np

class Reconstructor:
    def __init__(self, sampled_signal: signal):
        self.sampled_signal = sampled_signal

    def reconstruct_shannon(self, t: np.ndarray, sampling_frequency):
        x_vec = self.sampled_signal.x_vec
        y_vec = self.sampled_signal.y_vec

        # Whittaker-Shannon interpolation formula
        y_interp = np.zeros_like(t)
        for i, t_val in enumerate(t):
            y_interp[i] = np.sum(y_vec * np.sinc((x_vec - t_val) * sampling_frequency))
        
        return signal(np.array(t), np.array(y_interp), signalType.CONTINUOUS)

    def reconstruct_linear(self, t: np.ndarray):
        x_vec = self.sampled_signal.x_vec
        y_vec = self.sampled_signal.y_vec

        y_interp = np.interp(t, x_vec, y_vec)
        return signal(t, y_interp, signalType.CONTINUOUS)

    def reconstruct_cubic_spline(self, t: np.ndarray):
        x_vec = self.sampled_signal.x_vec
        y_vec = self.sampled_signal.y_vec

        cs = CubicSpline(x_vec, y_vec)
        y_interp = cs(t)
        return signal(t, y_interp, signalType.CONTINUOUS)
    
    def reconstruct_zero_order_hold(self, t: np.ndarray):
        x_vec = self.sampled_signal.x_vec  # Discrete time points of sampled signal
        y_vec = self.sampled_signal.y_vec  # Discrete sample values

        # Initialize array for interpolated values
        y_interp = np.zeros_like(t)

        # Loop over each interval between samples and hold the previous sample's value
        for i in range(len(x_vec) - 1):
            # Find indices in `t` that fall within the current interval
            indices = (t >= x_vec[i]) & (t < x_vec[i + 1])
            # Assign the value of `y_vec[i]` to all points in this interval
            y_interp[indices] = y_vec[i]

        # For the final interval, hold the last sample's value
        y_interp[t >= x_vec[-1]] = y_vec[-1]

        # Return the reconstructed signal as a continuous-type signal
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


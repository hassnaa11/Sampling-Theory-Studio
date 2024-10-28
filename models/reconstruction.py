from models.signal import signal, signalType
from scipy.interpolate import CubicSpline
import numpy as np
from scipy.interpolate import RBFInterpolator

class Reconstructor:
    def __init__(self, sampled_signal: signal):
        self.sampled_signal = sampled_signal

    def reconstruct_shannon(self, t: np.ndarray, sampling_frequency):
        # print("t = ", t)
        # print("sampling freq = ", sampling_frequency)
        x_vec = self.sampled_signal.x_vec
        y_vec = self.sampled_signal.y_vec

        # Whittaker-Shannon interpolation formula
        y_interp = np.zeros_like(t)
        
        for i, t_val in enumerate(t):
            y_interp[i] = np.sum(y_vec * np.sinc((x_vec - t_val) * sampling_frequency))
        
        # print("y_interp = ", y_interp)
        # print("len(y_interp) = ", len(y_interp))
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
        x_vec = self.sampled_signal.x_vec  
        y_vec = self.sampled_signal.y_vec  
        y_interp = np.zeros_like(t)
        for i in range(len(x_vec) - 1):
            indices = (t >= x_vec[i]) & (t < x_vec[i + 1])
            y_interp[indices] = y_vec[i]
        y_interp[t >= x_vec[-1]] = y_vec[-1]
        return signal(np.array(t), np.array(y_interp), signalType.CONTINUOUS)
    
    def reconstruct_nearest_neighbor(self, t: np.ndarray):
        
        x_vec = self.sampled_signal.x_vec
        y_vec = self.sampled_signal.y_vec
        y_interp = np.zeros_like(t)
        for i in range(len(t)):
            idx = np.argmin(np.abs(x_vec - t[i]))
            y_interp[i] = y_vec[idx]
        return signal(np.array(t), np.array(y_interp), signalType.CONTINUOUS)
        
    def reconstruct_RBF(self, t: np.ndarray, degree=3):
        x_vec = self.sampled_signal.x_vec.reshape(-1, 1)  # Reshape for RBF
        y_vec = self.sampled_signal.y_vec

        rbf_interpolator = RBFInterpolator(x_vec, y_vec)
        y_interp = rbf_interpolator(t.reshape(-1, 1))  # Reshape t for RBF

        return signal(np.array(t), np.array(y_interp).flatten(), signalType.CONTINUOUS)

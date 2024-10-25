from models.signal import signal, signalType
import numpy as np

class Sampler:
    # Takes a CONTINUOUS time signal 
    def __init__(self, signal: signal):
        if signal.signal_type != signalType.CONTINUOUS:
            raise ValueError("Sampler only accepts continuous time signals.")
        self.signal = signal
    
    # Outputs a DISCRETE time signal sampled at f_sample
    # using Nyquist–Shannon sampling theorem
    def sample(self, f_sampling: int):
        x_vec = self.signal.x_vec
        y_vec = self.signal.y_vec
        signal_type = signalType.DISCRETE

        #Sampling the signal
        x_sampled = np.arange(x_vec[0], x_vec[-1], 1/f_sampling)
        y_sampled = np.interp(x_sampled, x_vec, y_vec)
        return signal(x_sampled, y_sampled, signal_type)
    
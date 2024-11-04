import numpy as np
import matplotlib.pyplot as plt

# Define the signal and noise parameters
fs = 500  # Sample rate
t = np.linspace(0, 1, fs)  # Time vector for 1 second
signal = np.sin(2 * np.pi * 5 * t)  # Example 5 Hz sine wave signal
snr_dB = 20  # Desired SNR level in dB

# Function to add noise
def add_noise(signal, snr_dB):
    # Calculate the signal power
    signal_power = np.mean(signal**2)
    # Convert SNR from dB to a linear scale
    snr_linear = 10**(snr_dB / 10)
    # Calculate the noise power
    noise_power = signal_power / snr_linear
    # Generate white Gaussian noise and scale
    noise = np.sqrt(noise_power) * np.random.normal(size=signal.shape)
    # Add noise to the signal
    noisy_signal = signal + noise
    return noisy_signal

# Generate the noisy signal
noisy_signal = add_noise(signal, snr_dB)

# Plot the original and noisy signals
plt.figure(figsize=(12, 6))
plt.plot(t, signal, label="Original Signal", color="blue")
plt.plot(t, noisy_signal, label=f"Noisy Signal (SNR = {snr_dB} dB)", color="orange", alpha=0.7)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title("Signal with Additive Noise")
plt.legend()
plt.grid(True)
plt.show()

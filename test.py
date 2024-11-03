import numpy as np
import matplotlib.pyplot as plt

# Function to create a sharper triangle wave using the sum of cosines (Fourier series)
def create_sharp_triangle_wave(num_harmonics, time_points):
    triangle_wave = np.zeros_like(time_points)
    
    for k in range(1, num_harmonics + 1, 2):  # Only odd harmonics (1, 3, 5,...)
        # Calculate the magnitude for the k-th harmonic
        magnitude = (8 / (np.pi ** 2)) * (1 / (k ** 2)) * (-1 if (k // 2) % 2 else 1)
        
        # Sum each cosine term with decreasing magnitude
        triangle_wave += magnitude * np.cos(2 * np.pi * k * time_points)
    
    return triangle_wave

# Parameters
time_points = np.linspace(0, 1, 1000)  # Time points
num_harmonics = 100  # Increase the number of harmonics for sharper peaks

# Generate the triangle wave signal
triangle_wave = create_sharp_triangle_wave(num_harmonics, time_points)

# Plot the triangle wave
plt.plot(time_points, triangle_wave, label="Triangle Wave")
plt.title("Triangle Wave Signal (using Fourier series with more harmonics)")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()
plt.legend()
plt.show()

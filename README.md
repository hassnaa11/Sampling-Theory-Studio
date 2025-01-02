# Sampling-Theory Studio

## Introduction

Sampling-Theory Studio is a desktop application that demonstrates the importance of the Nyquist-Shannon sampling theorem. The application allows users to sample and recover signals, explore reconstruction methods, and visualize frequency-domain behavior to ensure signal integrity.

This project helps validate the Nyquist rate while showcasing the consequences of sampling below or above this rate.

---

## Features

### 1. Sample & Recover

- Load a mid-length signal (~1000 points).
- Visualize and sample it at different frequencies.
- Recover the original signal using various reconstruction methods:
  - Whittaker–Shannon
  - Linear
  - Zero-order hold
  - nearest_neighbor
  - Cubic Spline
  - Rational Polynomial Fit (RPF) interpolation

Four graphs are displayed:

1. Original Signal with Sampled Points
2. Reconstructed Signal
3. Difference Between Original and Reconstructed Signal
4. Frequency Domain Analysis (to detect aliasing)

---

### 2. Load & Compose

- Load a signal from a file or compose one using the built-in signal mixer.
- Add multiple sinusoidal components with adjustable frequencies and magnitudes.
- Remove individual components from the mixed signal.

---

### 3. Additive Noise

- Add noise to the loaded signal with custom Signal-to-Noise Ratio (SNR).
- Visualize the dependency of noise effects on signal frequency.

---

### 4. Real-Time Sampling & Recovery

- Instantaneous updates upon user changes (no refresh or update buttons).

---

### 5. Reconstruction Methods

- Choose between various reconstruction methods via a combo box.
- Compare pros and cons of each method using example signals.

---

### 6. Resizable UI

- The application supports resizing without distorting the layout or graphs.

---

### 7. Different Sampling Scenarios

- Prepares at least three synthetic signal examples:

  1. **Case 1**: Mix of 4Hz and 10Hz sinusoidals with amplitudes 5 and 5.
  2. **Case 2**: Mix of 6Hz and 4Hz sinusoidals with amplitudes 6 and 6, and the same phase.
  3. **Case 3**: Mix of 5Hz and 5Hz sinusoidals with amplitudes 1 and 0.5, and phases 90° and 0°.

---

## Usage

1. Install requirements:

   ```bash
   git install -r requirements.txt 
   ```
2. Clone the repository:

   ```bash
   git clone "https://github.com/hassnaa11/Sampling-Theory-Studio.git"  
   ```
3. Run the program:

   ```bash
   python program.py  
   ```

---

## Demonstration Videos

1. **Test Case Demonstration**

   Click the image to watch the video.

2. **Full Program Demonstration**

   Click the image to watch the video.

---
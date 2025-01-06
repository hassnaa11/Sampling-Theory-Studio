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

### 6. Different Sampling Scenarios

- Prepares at least three synthetic signal examples:

  1. **Case 1**: Mix of 4Hz and 10Hz sinusoidals with amplitudes 5 and 5.
    Description: This case combines two sinusoids with distinct frequencies (4Hz and 10Hz) but equal amplitudes (5). It simulates a scenario where signals with varying frequencies and similar energy levels interfere.

    Expected Outcome: Demonstrates the behavior of mixed-frequency signals, allowing evaluation of the system's ability to handle and reconstruct signals with frequency separation.

  2. **Case 2**: Mix of 6Hz and 4Hz sinusoidals with amplitudes 6 and 6, and the same phase.
    Description: A combination of two sinusoids (6Hz and 4Hz) with identical amplitudes (6) and the same initial phase. This case introduces phase coherence between components.

    Expected Outcome: Highlights the effect of phase alignment on signal reconstruction and the resulting waveform's characteristics.

  3. **Case 3**: Mix of 5Hz and 5Hz sinusoidals with amplitudes 1 and 1, and phases 180° and 0°.
    Description: Combines two sinusoids of the same frequency (5Hz) but opposite phases (180° and 0°) with equal amplitudes (1). This scenario explores destructive interference.

    Expected Outcome: Demonstrates how phase differences influence signal cancellation and overall amplitude, testing the system's handling of phase-aligned signals.

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

## Contributors

<table align="center" width="100%">
  <tr>
     <td align="center" width="20%">
      <a href="https://github.com/Emaaanabdelazeemm">
        <img src="https://github.com/Emaaanabdelazeemm.png?size=100" style="width:80%;" alt="Emaaanabdelazeemm"/>
      </a>
      <br />
      <a href="https://github.com/Emaaanabdelazeemm">Eman Abdelazeemm</a>
    </td>
    <td align="center" width="20%">
      <a href="https://github.com/hassnaa11">
        <img src="https://github.com/hassnaa11.png?size=100" style="width:80%;" alt="hassnaa11"/>
      </a>
      <br />
      <a href="https://github.com/hassnaa11">Hassnaa Hossam</a>
    </td>
   <td align="center" width="20%">
      <a href="https://github.com/Ayat-Tarek">
        <img src="https://github.com/Ayat-Tarek.png?size=100" style="width:80%;" alt="Ayat-Tarek"/>
      </a>
      <br />
      <a href="https://github.com/Ayat-Tarek">Ayat Tarek</a>
    </td>
    <td align="center" width="20%">
      <a href="https://github.com/shahdragab89">
        <img src="https://github.com/shahdragab89.png?size=100" style="width:80%;" alt="shahdragab89"/>
      </a>
      <br />
      <a href="https://github.com/shahdragab89">shahd Ragab</a>
    </td>
    <td align="center" width="20%">
      <a href="https://github.com/yasmine-msg79">
        <img src="https://github.com/yasmine-msg79.png?size=100" style="width:80%;" alt="yasmine-msg79"/>
      </a>
      <br />
      <a href="https://github.com/yasmine-msg79">Yasmine Mahmoud</a>
    </td>
  </tr>
</table>


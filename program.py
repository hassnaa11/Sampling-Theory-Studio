from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore
from gui_2 import Ui_MainWindow
from mixer import Mixer

from PyQt5.QtWidgets import QFileDialog
import pyqtgraph as pg
import sys
import pandas as pd
from models.signal import signal, signalType  
from models.sampler import Sampler           
from models.reconstruction import Reconstructor 
import numpy as np

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.open_file_button.clicked.connect(self.open_file)
        self.ui.actual_radioButton.toggled.connect(self.update_slider_range)
        self.ui.normalized_radioButton.toggled.connect(self.update_slider_range)
        self.ui.fs_horizontalSlider.valueChanged.connect(self.set_sampling_frequency)
        
        # Set initial properties
        self.signal = None
        self.sampled_signal = None
        self.reconstructed_signal = None
        self.sampling_curve = None
        self.reconstruct_curve = None
        self.difference_curve = None  
        self.sampling_frequency = 700 # this would be changed by the slider
        self.freq_values = []
        self.max_frequency = 150 #this will be calculated by the function 

        self.ui.methods_comboBox.currentIndexChanged.connect(self._reconstruct)
        
        self.is_mixer_running = False
        self.mixer = Mixer(self.ui.tableWidget, self.ui.mixed_signal_graph, self.ui.tests_comboBox)
        self.ui.mixer_button.clicked.connect(self.mixSignals)
        self.ui.apply_button_2.clicked.connect(self.plot_composed_signal)

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open CSV", "", "CSV Files (*.csv);;All Files (*)")

        if file_name:
            self.plot_csv_data(file_name)

    def plot_csv_data(self, file_name):
        df = pd.read_csv(file_name, header=None, nrows=1000)  # Read CSV without a header
        df.columns = ['x', 'y']

        if 'x' in df.columns and 'y' in df.columns:
            x = np.array(df['x'])
            y = np.array(df['y'])
            
            # Initialize the signal
            self.signal = signal(x, y, signalType.CONTINUOUS)

            # Calculate the maximum frequency for the loaded signal
            self.calculate_max_frequency(x, y)

            # Clear any previous plots
            self.ui.original_signal_graph.plotItem.clear() 
            self.ui.reconstructed_signal_graph.plotItem.clear()

            # Plot the original signal
            self.ui.original_signal_graph.plot(x, y, pen='w')

            # Set the range for both plots to match the signal size
            self.ui.original_signal_graph.plotItem.getViewBox().setRange(xRange=(x.min(), x.max()), yRange=(y.min(), y.max()))
            self.ui.reconstructed_signal_graph.plotItem.getViewBox().setRange(xRange=(x.min(), x.max()), yRange=(y.min(), y.max()))
            self.ui.difference_signal_graph.plotItem.getViewBox().setRange(xRange=(x.min(), x.max()), yRange=(y.min(), y.max()))

            # Sample and reconstruct signal after loading
            self._resample()
            self._reconstruct()

            self.ui.fs_value_label.setText(f"{self.sampling_frequency:.2f} Hz")

    
    def calculate_max_frequency(self, x, y):
        fs = 1/(x[1] - x[0])
        self.max_frequency = fs/2

        print(f"Calculated maximum frequency: {self.max_frequency} Hz")
        # # Subtract the mean to remove DC component
        # y = y - np.mean(y)
        
        # # Calculate the sampling rate
        # time_intervals = np.diff(x)
        # avg_time_interval = np.mean(time_intervals)
        # sampling_rate = 1 / avg_time_interval  # in Hz

        # # Perform FFT with zero-padding to increase frequency resolution
        # N = len(y)
        # N_fft = 2**self.next_power_of_2(N)  # Use the next power of 2 for FFT length
        # fft_vals = np.fft.fft(y, N_fft)
        # fft_freqs = np.fft.fftfreq(N_fft, d=avg_time_interval)

        # # Use only the positive frequencies (as FFT is symmetric)
        # positive_freq_indices = np.where(fft_freqs > 0)  # Strictly positive frequencies
        # positive_freqs = fft_freqs[positive_freq_indices]
        # positive_fft_vals = np.abs(fft_vals[positive_freq_indices])

        # # Find the peak frequency (highest amplitude)
        # peak_freq_index = np.argmax(positive_fft_vals)
        # self.max_frequency = positive_freqs[peak_freq_index]

    def next_power_of_2(self, x):
        return int(np.ceil(np.log2(x)))

    def update_slider_range(self):
        print("i am in update slider")
        if self.ui.actual_radioButton.isChecked():
            self.ui.fs_horizontalSlider.setRange(1, 1000)
            self.ui.fs_horizontalSlider.setSingleStep(1)
            self.ui.fs_horizontalSlider.setValue(self.sampling_frequency) 
            print("Slider in 'Actual' mode: 1 to 1150")
        else:
            print(f"max frequency in update slider{self.max_frequency}")
            self.freq_values = [1 * self.max_frequency, 2 * self.max_frequency, 3 * self.max_frequency, 4 * self.max_frequency]
            self.ui.fs_horizontalSlider.setRange(0, len(self.freq_values) - 1)
            self.ui.fs_horizontalSlider.setSingleStep(1)
            self.ui.fs_horizontalSlider.setValue(0)
            print("Slider in 'Normalized' mode: four max frequencies")

    def set_sampling_frequency(self, value):
        if self.ui.normalized_radioButton.isChecked():
            self.sampling_frequency = self.freq_values[value]
        else:
            self.sampling_frequency = value

        # Update the label with the current frequency
        self.ui.fs_value_label.setText(f"{self.sampling_frequency:.2f} Hz")
        print(f"Current sampling frequency: {self.sampling_frequency}")

        self._resample()
        self._reconstruct()

    def plot_composed_signal(self):
        self.mixer.stop()
        
        self.ui.original_signal_graph.plotItem.clear()  
        self.ui.reconstructed_signal_graph.plotItem.clear()
                
        if int(self.mixer.max_frequency) != 0 and np.any(self.mixer.composed_x_data != 0) and np.any(self.mixer.composed_y_data != 0):
            self.sampling_frequency = 2 * int(self.mixer.max_frequency)
            
            x = self.mixer.composed_x_data
            y = self.mixer.composed_y_data    
        
            # Initialize the signal
            self.signal = signal(x, y, signalType.CONTINUOUS)

            # Clear any previous plots
            self.ui.original_signal_graph.plotItem.clear() 
            self.ui.reconstructed_signal_graph.plotItem.clear()

            # Plot the original signal
            self.ui.original_signal_graph.plot(x, y, pen='w')

            # Set the range for both plots to match the signal size
            self.ui.original_signal_graph.plotItem.getViewBox().setRange(xRange=(x.min(), x.max()), yRange=(y.min(), y.max()))
            self.ui.reconstructed_signal_graph.plotItem.getViewBox().setRange(xRange=(x.min(), x.max()), yRange=(y.min(), y.max()))
            self.ui.difference_signal_graph.plotItem.getViewBox().setRange(xRange=(x.min(), x.max()), yRange=(y.min(), y.max()))

            # Sample and reconstruct signal after loading
            self._resample() 
        else:
            self.ui.original_signal_graph.plotItem.clear()  
            self.ui.reconstructed_signal_graph.plotItem.clear()         
            

    def _resample(self):
        sampler = Sampler(self.signal)
        self.sampled_signal = sampler.sample(self.sampling_frequency)

        # Clear previous sampling plot 
        if self.sampling_curve is not None:
            self.ui.original_signal_graph.removeItem(self.sampling_curve)

        # Plot sampled points on the original graph
        self.sampling_curve = self.ui.original_signal_graph.plot(
            self.sampled_signal.x_vec,
            self.sampled_signal.y_vec,
            pen=None, symbol='x',
            symbolBrush=pg.mkBrush(255, 0, 0, 255)  # Red 'x' markers
        )

    def _reconstruct(self):
        if not self.sampled_signal:
            return  

        reconstructor = Reconstructor(self.sampled_signal)
        
        # Generate time points for reconstruction
        t = np.linspace(self.signal.x_vec[0], self.signal.x_vec[-1], 1000)
        method = self.ui.methods_comboBox.currentText()

        if method == "whittaker_shannon":
                    self.reconstructed_signal = reconstructor.reconstruct_shannon(t, self.sampling_frequency)
        elif method == "RBF interpolation":
                    self.reconstructed_signal = reconstructor. reconstruct_RBF(t)
        elif method == "nearest_neighbor":
                    self.reconstructed_signal=reconstructor.reconstruct_nearest_neighbor(t)
        elif method == "Linear":
            self.reconstructed_signal = reconstructor.reconstruct_linear(t)
        elif method == "Cubic Spline":
            self.reconstructed_signal = reconstructor.reconstruct_cubic_spline(t)
        elif method=="Zero-Order Hold":
            self.reconstructed_signal = reconstructor. reconstruct_zero_order_hold(t)

        # Clear previous reconstructed plot
        if self.reconstruct_curve is not None:
            self.ui.reconstructed_signal_graph.removeItem(self.reconstruct_curve)

        # Plot the reconstructed signal
        self.reconstruct_curve = self.ui.reconstructed_signal_graph.plot(
            self.reconstructed_signal.x_vec,
            self.reconstructed_signal.y_vec,
            pen=pg.mkPen(color=(255, 255, 255))  # Green pen
        )

        # Plot the difference signal
        self._calculate_difference()

    def _calculate_difference(self):
        if not self.signal or not self.reconstructed_signal:
            return
        
        # Define x_diff to be the same as the original signal's x-values
        x_diff = self.signal.x_vec
        
        # Interpolate the reconstructed signal to match the original signal's x values
        y_interp = np.interp(x_diff, self.reconstructed_signal.x_vec, self.reconstructed_signal.y_vec)
        
        # Calculate the difference
        y_diff = self.signal.y_vec - y_interp

        # Clear any previous difference plot
        self.ui.difference_signal_graph.plotItem.clear()

        # Plot the difference signal
        self.ui.difference_signal_graph.plot(x_diff, y_diff, pen=pg.mkPen(color=(255, 0, 0)))  # Red pen for difference signal

    def mixSignals(self):
        self.is_mixer_running = not self.is_mixer_running 
        if self.is_mixer_running and self.mixer.running == False:
            self.mixer.start()
        else:
            self.mixer.stop()  
            
    # to stop mixer thread before exit the program        
    def closeEvent(self, event): 
        self.mixer.stop() 
        event.accept()         

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    ui = MainWindow()
    ui.show()
    app.exec_()        
    
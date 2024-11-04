from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore
from gui_2 import Ui_MainWindow
from mixer import Mixer

from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QTableWidgetItem
import pyqtgraph as pg
import sys
import pandas as pd
from models.signal import signal, signalType  
from models.sampler import Sampler           
from models.reconstruction import Reconstructor 
import numpy as np
from scipy.signal import butter, filtfilt

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.open_file_button.clicked.connect(self.open_file)

        self.ui.actual_radioButton.setChecked(True)
        self.ui.actual_radioButton.toggled.connect(self.update_slider_range)
        self.ui.normalized_radioButton.toggled.connect(self.update_slider_range)
        self.ui.fs_horizontalSlider.valueChanged.connect(self.set_sampling_frequency)
        self.ui.snr_horizontalSlider.valueChanged.connect(self.set_SNR)
        self.ui.snr_horizontalSlider.setRange(1,50)
        self.SNR = 1
        self.ui.snr_value_label.setText(f"{self.SNR} SNR")
        self.ui.noise_checkBox.setChecked(False)
        self.ui.noise_checkBox.clicked.connect(self.add_noise)
        self.ui.snr_horizontalSlider.setEnabled(False)
        
        # Set initial properties
        self.signal = None
        self.sampled_signal = None
        self.reconstructed_signal = None
        self.sampling_curve = None
        self.reconstruct_curve = None
        self.difference_curve = None  
        self.sampling_frequency = 700 
        self.ui.fs_horizontalSlider.setValue(self.sampling_frequency)  # Set slider to 700 on startup
        print(f"sampling frequecy initial:{self.sampling_frequency}")
        self.ui.fs_value_label.setText(f"{self.sampling_frequency:.2f} Hz")
        self.update_slider_range()
        self.init_equal_space()
        self.ui.side_bar_widget.hide()
        self.freq_values = []
        self.max_frequency = 150 #this will be calculated by the function 
        self.sidebar_visible = False
        self.ui.methods_comboBox.currentIndexChanged.connect(self._reconstruct)
        self.ui.tests_comboBox.currentIndexChanged.connect(self.test_cases)
        
        self.is_mixer_running = False
        self.mixer = Mixer(self.ui.tableWidget, self.ui.mixed_signal_graph)
        # self.ui.mixer_button.clicked.connect(self.toggle_sidebar)
        self.ui.mixer_button.clicked.connect(self.mixSignals)
        self.ui.apply_button_2.clicked.connect(self.plot_composed_signal)
        self.ui.error_frequency_toggle_button.toggled.connect(self.handle_radio_button)
       

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

            if(self.ui.noise_checkBox.isChecked()):
                self.add_noise()
            # Sample and reconstruct signal after loading
            self._resample()
            self._reconstruct()

            self.update_slider_range()

    def calculate_max_frequency(self, x, y):
        fs = 1/(x[1] - x[0])
        self.max_frequency = fs/2

        print(f"Calculated maximum frequency: {self.max_frequency} Hz")
        
    def update_slider_range(self):
        if self.ui.actual_radioButton.isChecked():
            # print(f"self,max_frequency = {self.max_frequency}")
            self.ui.fs_horizontalSlider.setRange(1, 10000)
            self.ui.fs_horizontalSlider.setSingleStep(1)
            self.ui.fs_horizontalSlider.setValue(int(self.sampling_frequency)) 
            self.ui.fs_value_label.setText(f"{self.sampling_frequency:.2f} Hz")
            print("Slider in 'Actual' mode: 1 to 1150")
        else:
            print(f"max frequency in update slider{self.max_frequency}")
            self.freq_values = [1 * self.max_frequency, 2 * self.max_frequency, 3 * self.max_frequency, 4 * self.max_frequency]
            self.ui.fs_horizontalSlider.setRange(0, len(self.freq_values) - 1)
            self.ui.fs_horizontalSlider.setSingleStep(1)
            self.ui.fs_horizontalSlider.setValue(0)
            self.set_sampling_frequency(0)  
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
        self.is_mixer_running = False
        print("i am in plot composed signal")
        
        self.ui.original_signal_graph.plotItem.clear()  
        self.ui.reconstructed_signal_graph.plotItem.clear()
        self.ui.difference_signal_graph.plotItem.clear()
        self.ui.frequancy_domain_graph.plotItem.clear()
        self.ui.side_bar_widget.hide() 
        self.sidebar_visible = not self.sidebar_visible
        self.centralWidget().layout().update() 

        if float(self.mixer.max_frequency) != 0 and np.any(self.mixer.composed_x_data != 0) and np.any(self.mixer.composed_y_data != 0):
            print("plot composed signal in main graph")
            self.sampling_frequency = 2 * float(self.mixer.max_frequency)
            self.max_frequency = float(self.mixer.max_frequency)
                
            x = self.mixer.composed_x_data
            y = self.mixer.composed_y_data  

            # Initialize the signal
            self.signal = signal(x, y, signalType.CONTINUOUS)

            # Plot the original signal
            self.ui.original_signal_graph.plot(x, y, pen='w')

            # Set the range for both plots to match the signal size
            self.ui.original_signal_graph.plotItem.getViewBox().setRange(xRange=(x.min(), x.max()), yRange=(y.min(), y.max()))
            self.ui.reconstructed_signal_graph.plotItem.getViewBox().setRange(xRange=(x.min(), x.max()), yRange=(y.min(), y.max()))

            if(self.ui.noise_checkBox.isChecked()):
                self.add_noise()
            # Sample and reconstruct signal after loading
            self._resample() 
            self._reconstruct()
            self.update_slider_range()
        else:
            self.ui.original_signal_graph.plotItem.clear()  
            self.ui.reconstructed_signal_graph.plotItem.clear() 
            self.ui.difference_signal_graph.plotItem.clear()
            self.ui.frequancy_domain_graph.plotItem.clear()

    def _resample(self):
        if(self.ui.noise_checkBox.isChecked()):
            sampler = Sampler(self.noisy_signal)
        else:
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
        t = np.linspace(self.signal.x_vec[0], self.signal.x_vec[-1], 1000)
        
        method = self.ui.methods_comboBox.currentText()

        #  # Ensure high-frequency sampling leads to good interpolation
        # if self.sampling_frequency >= 2 * self.max_frequency:
        #     t_high = np.linspace(self.signal.x_vec[0], self.signal.x_vec[-1], 2000)  # Higher resolution for reconstruction
        #     self.reconstructed_signal = reconstructor.reconstruct_shannon(t_high, self.sampling_frequency)


        if method == "whittaker_shannon":
                    self.reconstructed_signal = reconstructor.reconstruct_shannon(t, self.sampling_frequency)
        elif method == "Zero-Order Hold":
                    self.reconstructed_signal = reconstructor.reconstruct_zero_order_hold(t)
        elif method == "nearest_neighbor":
                    self.reconstructed_signal=reconstructor.reconstruct_nearest_neighbor(t)
        elif method == "Linear":
            self.reconstructed_signal = reconstructor.reconstruct_linear(t)
        elif method == "Cubic Spline":
            self.reconstructed_signal = reconstructor.reconstruct_cubic_spline(t)
        elif method == "RBF interpolation":
            self.reconstructed_signal = reconstructor.reconstruct_RBF(t)

        
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
        self.create_frequency_domain(self.ui.frequancy_domain_graph)

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
            self.ui.side_bar_widget.show()
            self.sidebar_visible = not self.sidebar_visible
            self.centralWidget().layout().update() 
            self.mixer.start()

        else:
            self.mixer.stop() 
            self.ui.side_bar_widget.hide() 
            self.sidebar_visible = not self.sidebar_visible
            self.centralWidget().layout().update() 

    # to stop mixer thread before exit the program        
    def closeEvent(self, event): 
        self.mixer.stop() 
        event.accept()  
     
    def set_SNR(self, value):
        if self.signal:
            self.SNR = value 
            if(self.ui.noise_checkBox.isChecked()):
                self.ui.snr_value_label.setText(f"{self.SNR} SNR")
            print("SNR: ", self.SNR)
            self.add_noise()

    def add_noise(self): 
        if self.signal:
            
            # signal power = mean value in the signal  
            signal_power = np.mean(self.signal.y_vec**2)
            # convert dB SNR to linear
            linear_snr = 10 ** (self.SNR / 10)
            # SNR = Signal / Noise
            noise_power = np.sqrt(signal_power) / linear_snr 
            # White Gaussian noise (normal noise)
            noise = noise_power * np.random.normal(size = self.signal.y_vec.shape)
            noisy_signal = noise + self.signal.y_vec
                        
            self.noisy_signal = signal(self.signal.x_vec, noisy_signal, signalType.CONTINUOUS) 

            self.ui.original_signal_graph.plotItem.clear() 
            self.ui.reconstructed_signal_graph.plotItem.clear()

            if(self.ui.noise_checkBox.isChecked()):
                self.ui.snr_horizontalSlider.setEnabled(True)
                # Plot the noisy signal in the original graph
                self.ui.original_signal_graph.plot(self.signal.x_vec, noisy_signal , pen='w')

                # Set the range for both plots to match the signal size
                self.ui.original_signal_graph.plotItem.getViewBox().setRange(xRange=(self.signal.x_vec.min(), self.signal.x_vec.max()), yRange=(noisy_signal.min(), noisy_signal.max()))
                self.ui.reconstructed_signal_graph.plotItem.getViewBox().setRange(xRange=(self.signal.x_vec.min(), self.signal.x_vec.max()), yRange=(noisy_signal.min(), noisy_signal.max()))
            else:  
                self.ui.snr_horizontalSlider.setEnabled(False)
                # Plot the original signal in the original graph
                self.ui.original_signal_graph.plot(self.signal.x_vec, self.signal.y_vec , pen='w')

                # Set the range for both plots to match the signal size
                self.ui.original_signal_graph.plotItem.getViewBox().setRange(xRange=(self.signal.x_vec.min(), self.signal.x_vec.max()), yRange=(self.signal.y_vec.min(), self.signal.y_vec.max()))
                self.ui.reconstructed_signal_graph.plotItem.getViewBox().setRange(xRange=(self.signal.x_vec.min(), self.signal.x_vec.max()), yRange=(self.signal.y_vec.min(), self.signal.y_vec.max()))
                
            # Sample and reconstruct signal
            self._resample()
            self._reconstruct()      

    def create_frequency_domain(self, frequency_graph):
        
        if not self.signal or not self.reconstructed_signal:
            return

        self.ui.frequancy_domain_graph.clear()

        N = len(self.reconstructed_signal.x_vec)
        dt = self.reconstructed_signal.x_vec[1] - self.reconstructed_signal.x_vec[0]   
        self.frequencies = np.fft.fftfreq(N, dt)

        self.amplitude = (np.abs(np.fft.fft(self.reconstructed_signal.y_vec))/ N) 


        # Plot original signal
        self.frequency_line = frequency_graph.plot(
            self.frequencies,
            self.amplitude,
            pen=pg.mkPen(color="yellow"),
            name='Original Signal'
        )

        # Plot aliased components
       
        self.after_band_width_line = frequency_graph.plot(
        self.frequencies + self.sampling_frequency,
        self.amplitude,
        pen=pg.mkPen(color="red"),
        name='After Sampling Frequency'
        )
        self.before_band_width_line = frequency_graph.plot(
            - self.frequencies - self.sampling_frequency,
            self.amplitude,
            pen=pg.mkPen(color="red"),
            name='Before Sampling Frequency'
        )
        # Set the range 
        frequency_graph.plotItem.getViewBox().setRange(
            xRange=(-self.sampling_frequency, self.sampling_frequency),  
            yRange=(0, self.amplitude.max() * 1.5) 
        )
        frequency_graph.showGrid(x=True, y=True, alpha=0.3)


    def handle_radio_button(self, checked):
        if checked:
            self.ui.error_frequency_toggle_button.setText("Show Error Difference")
            self.ui.stackedWidget.setCurrentIndex(1)  # Frequency Domain page
        else:
            self.ui.error_frequency_toggle_button.setText("Show Frequency Domain")
            self.ui.stackedWidget.setCurrentIndex(0)  # Error Difference page

    def init_equal_space(self):
        self.centralWidget().layout().setStretch(0, 1)  # Left part
        self.centralWidget().layout().setStretch(1, 1)  # Sidebar

    def test_cases(self):

        test=self.ui.tests_comboBox.currentText()

        if test == "Test":
        # Optionally, clear the table or show a message indicating no test is selected
            return
        if test == "Test Case 1":
            self.ui.tableWidget.setRowCount(0)  # Clear previous rows

            # Amplitude Modulation Example with Carrier and Envelope:
            # Row 0: Carrier Signal
            self.ui.tableWidget.insertRow(0)
            self.ui.tableWidget.setItem(0, 0, QTableWidgetItem(str(4)))  # Frequency: 15 Hz (Carrier)
            self.ui.tableWidget.setItem(0, 1, QTableWidgetItem(str(5)))   # Amplitude: 1 (Carrier)
            self.ui.tableWidget.setItem(0, 2, QTableWidgetItem(str(0)))   # Phase: 0 (Carrier)
            icon_item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget.setItem(0, 3, icon_item)
            icon_item.setIcon(self.mixer.remove_icon)
            
            # Row 1: Envelope Signal
            self.ui.tableWidget.insertRow(1)
            self.ui.tableWidget.setItem(1, 0, QTableWidgetItem(str(10)))  # Frequency: 0.5 Hz (Envelope)
            self.ui.tableWidget.setItem(1, 1, QTableWidgetItem(str(5)))  # Amplitude: 0.5 (Envelope)
            self.ui.tableWidget.setItem(1, 2, QTableWidgetItem(str(0)))    # Phase: 0 (Envelope)


        elif test=="Test Case 2":
            self.ui.tableWidget.setItem(0, 0, QTableWidgetItem(str(6)))  # Frequency
            self.ui.tableWidget.setItem(0, 1, QTableWidgetItem(str(6)))  # Amplitude
            self.ui.tableWidget.setItem(0, 2, QTableWidgetItem(str(0)))  # Phase
            icon_item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget.setItem(0, 3, icon_item)
            icon_item.setIcon(self.mixer.remove_icon)
            # Check if the second row exists; if not, insert it
            if self.ui.tableWidget.rowCount() < 2:
                self.ui.tableWidget.insertRow(1)
            # Set values for the second row
            self.ui.tableWidget.setItem(1, 0, QTableWidgetItem(str(4)))  # Frequency
            self.ui.tableWidget.setItem(1, 1, QTableWidgetItem(str(6)))  # Amplitude
            self.ui.tableWidget.setItem(1, 2, QTableWidgetItem(str(0)))  # Phase

        elif test == "Test Case 3":
            self.ui.tableWidget.setRowCount(0)  # Clear previous rows

            # Phase Cancellation Example:
            self.ui.tableWidget.insertRow(0)
            self.ui.tableWidget.setItem(0, 0, QTableWidgetItem(str(5)))  # Frequency: 4 Hz
            self.ui.tableWidget.setItem(0, 1, QTableWidgetItem(str(1)))  # Amplitude: 1
            self.ui.tableWidget.setItem(0, 2, QTableWidgetItem(str(90)))  # Phase: 0
            icon_item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget.setItem(0, 3, icon_item)
            icon_item.setIcon(self.mixer.remove_icon)

            self.ui.tableWidget.insertRow(1)
            self.ui.tableWidget.setItem(1, 0, QTableWidgetItem(str(5)))  # Frequency: 4 Hz
            self.ui.tableWidget.setItem(1, 1, QTableWidgetItem(str(0.5)))  # Amplitude: 1
            self.ui.tableWidget.setItem(1, 2, QTableWidgetItem(str(0)))  # Phase: 180 degrees (π)
            


        # elif test == "Test Case 3":
        #     self.ui.tableWidget.setRowCount(0)  # Clear previous rows

        #     # Square wave harmonic components for different sampling rates
        #     sampling_cases = [
        #         {"Frequency": 1, "Amplitude": 1, "Phase": 0},  # 1 Hz fundamental
        #         {"Frequency": 3, "Amplitude": 1/3, "Phase": 0},  # 3rd harmonic
        #         {"Frequency": 5, "Amplitude": 1/5, "Phase": 0},  # 5th harmonic
        #         {"Frequency": 7, "Amplitude": 1/7, "Phase": 0},  # 7th harmonic
        #         # Add more harmonics if necessary for the scenario
        #     ]

        #     # Example case for a 20 Hz sampling rate
        #     for index, harmonic in enumerate(sampling_cases):
        #         if self.ui.tableWidget.rowCount() <= index:
        #             self.ui.tableWidget.insertRow(index)
        #         self.ui.tableWidget.setItem(index, 0, QTableWidgetItem(str(harmonic["Frequency"])))  # Frequency
        #         self.ui.tableWidget.setItem(index, 1, QTableWidgetItem(str(harmonic["Amplitude"])))  # Amplitude
        #         self.ui.tableWidget.setItem(index, 2, QTableWidgetItem(str(harmonic["Phase"])))  # Phase

        #     # Example demonstration messages (optional) to show the difference in reconstruction:
        #     # At 20 Hz, capture several harmonics and reconstruct the square wave accurately.
        #     # At 8 Hz, capture limited harmonics, missing details but retaining the basic shape.
        #     # At 4 Hz, demonstrate the effects of aliasing causing severe distortion.

        #     # If you want to automate more details, such as dynamically changing the sampling rate and plotting the waveforms, additional code may be needed.
            
        # # elif test=="Test Case 1":

             
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    ui = MainWindow()
    ui.show()
    app.exec_()        
    

    
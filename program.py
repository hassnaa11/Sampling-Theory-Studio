from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtCore

from gui import Ui_MainWindow

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


        # Set initial properties

        self.signal = None

        self.sampled_signal = None

        self.reconstructed_signal = None

        self.sampling_curve = None

        self.reconstruct_curve = None

        self.sampling_frequency = 700  # this would be changed by the slider


    def open_file(self):

        file_name, _ = QFileDialog.getOpenFileName(self, "Open CSV", "", "CSV Files (*.csv);;All Files (*)")


        if file_name:

            self.plot_csv_data(file_name)


    def plot_csv_data(self, file_name):

        df = pd.read_csv(file_name, header=None)  # Read CSV without a header

        df.columns = ['x', 'y']


        if 'x' in df.columns and 'y' in df.columns:

            x = np.array(df['x'])

            y = np.array(df['y'])
        

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


            # Sample and reconstruct signal after loading
            self._resample()
            self._reconstruct()


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
        

        reconstructor = Reconstructor(self.sampled_signal)
        

        # Generate time points for reconstruction

        t = np.linspace(self.signal.x_vec[0], self.signal.x_vec[-1], 1000)

        self.reconstructed_signal = reconstructor.reconstruct(t, self.sampling_frequency)


        # Clear previous reconstructed plot

        if self.reconstruct_curve is not None:

            self.ui.reconstructed_signal_graph.removeItem(self.reconstruct_curve)


        # Plot the reconstructed signal

        self.reconstruct_curve = self.ui.reconstructed_signal_graph.plot(

            self.reconstructed_signal.x_vec,

            self.reconstructed_signal.y_vec,

            pen=pg.mkPen(color=(0, 255, 0))  # Green pen
        )


if __name__ == "__main__":

    app = QtWidgets.QApplication([])

    ui = MainWindow()

    ui.show()

    app.exec_()        
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore
from gui import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog
import pyqtgraph as pg
import sys
import pandas as pd


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.open_file_button.clicked.connect(self.open_file)
    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open CSV", "", "CSV Files (*.csv);;All Files (*)")

        if file_name:
            self.plot_csv_data(file_name)

    def plot_csv_data(self, file_name):
        df = pd.read_csv(file_name, header=None)  # Read CSV without a header
        df.columns = ['x', 'y']
        print("hhhh")
        print("Columns in the DataFrame:", df.columns)
        if 'x' in df.columns and 'y' in df.columns:
            x = df['x']
            y = df['y']
            print(x[:5])
            self.ui.original_signal_graph.plotItem.clear() 
            self.ui.original_signal_graph.plot(x, y, pen='w')



        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    ui = MainWindow()
    ui.show()
    app.exec_()        
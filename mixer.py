import numpy as np
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import  QtGui, QtWidgets
class Mixer(QThread):
    update_data_signal = pyqtSignal(dict)

    def __init__(self, signals_table, preview_graph, tests_comboBox):
        super().__init__()
        self.signals_table = signals_table
        self.preview_graph = preview_graph
        self.tests_comboBox = tests_comboBox
        self.signals_table.insertRow(self.signals_table.rowCount())
        
        self.remove_icon = QtGui.QIcon()
        self.remove_icon.addPixmap(QtGui.QPixmap("images\icons8-remove-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.signals_table.cellClicked.connect(self.handleCellClick)
        
        self.signals_table.setStyleSheet("color: white")
        self.signals_data = {}
        self.running = False
        self.max_frequency = 0
        self.composed_x_data = 0
        self.composed_y_data = 0
        self.update_data_signal.connect(self.update_data)
        
        
    def getSignalInfo(self):
        signals_data = {}
        row_count = self.signals_table.rowCount()
        rows = 0
        self.max_frequency = 0
        for row in range(row_count):
            # print(row)
            if self.signals_table.item(row, 0) and self.signals_table.item(row, 1) and self.signals_table.item(row, 2):
                signals_data[row] = {
                    'Frequency': self.signals_table.item(row, 0).text(),
                    'Amplitude': self.signals_table.item(row, 1).text(),
                    'Phase'    : self.signals_table.item(row, 2).text()
                }
                rows += 1 # count rows that has data)

                if float(self.signals_table.item(row, 0).text()) > float(self.max_frequency):
                    self.max_frequency = self.signals_table.item(row, 0).text()
                    # print("max frequency: ", self.max_frequency)
                
        if not(self.signals_data == signals_data):
            print("will emit")
            self.signals_data = signals_data
            self.update_data_signal.emit(signals_data) 

                            
        # check if all rows have data then add new row and emit data 
        if rows == row_count: 
            icon_item = QtWidgets.QTableWidgetItem()
            self.signals_table.setItem(rows - 1, 3, icon_item)
            icon_item.setIcon(self.remove_icon)
            self.signals_table.insertRow(self.signals_table.rowCount())
            
    
    def plotMixedSignals(self):
        print("plot mixed signals")
        self.preview_graph.clear()
        self.composed_x_data = np.linspace(0, 2,1000)
        self.composed_y_data = 0
        # y = A*sin(2πfx + ϕ)
        for signal in self.signals_data.values():
            self.composed_y_data += np.sin(2*np.pi * float(signal['Frequency']) * self.composed_x_data + float(signal['Phase'])) * float(signal['Amplitude'])
        
        if np.any(self.composed_y_data != 0):
            self.preview_graph.plot( self.composed_x_data, self.composed_y_data, pen="w")
    
    def update_data(self, data):
        print("update data")
        self.signals_data = data 
        # print(self.signals_data)
        self.plotMixedSignals()
        
    def handleCellClick(self, row, col):
        if col == 3:
            if row in self.signals_data:
                del self.signals_data[row]
                self.signals_table.removeRow(row)
                self.plotMixedSignals()
    
    def run(self):
        self.running = True
        while self.running:
            self.getSignalInfo()
            # print("runn")  
    
    def stop(self):
        print("stop")
        self.running = False       
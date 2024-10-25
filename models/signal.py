from enum import Enum

class signalType(Enum):
    CONTINUOUS = 0
    DISCRETE = 1

class signal:

    def __init__(self, x_vec, y_vec, signal_type: signalType = signalType.CONTINUOUS):

        self.x_vec = x_vec
        self.y_vec = y_vec
        self.signal_type = signal_type

    
       

import numpy as np

class Quadripole:
    def __init__(self, V1 = None, I1 = None, V2 = None, I2  = None):
        self.tensions = [V1, V2]
        self.currents = [I1, I2]
        pass
    
class SeriesImpedance(Quadripole):
    def __init__(self, z, V1 = None, I1 = None, V2 = None, I2  = None):
        super().__init__(V1, I1, V2, I2)
        self.net_mtrx = np.array([[1, z], 
                                 [0 ,1]])
        pass
    
class ShuntAdmittance(Quadripole):
    def __init__(self, z, V1 = None, I1 = None, V2 = None, I2  = None):
        super().__init__(V1, I1, V2, I2)
        self.net_mtrx = np.array([1, 0],
                                 [1/z ,0])
        pass
    
class PiCircuit(Quadripole):
    def __init__(self, z, y1, y2, V1 = None, I1 = None, V2 = None, I2  = None):
        super().__init__(V1, I1, V2, I2)
        self.net_mtrx = np.array([1 + y2*z, z], 
                                 [y1 + y2 + y1*y2*z , 1+y1*z])
        pass

class Transformer(Quadripole):
    def __init__(self, n, z1, z2, y, V1 = None, I1 = None, V2 = None, I2  = None):
        super().__init__(V1, I1, V2, I2)
        self.net_mtrx = np.array([1/n * 1/(1+ y*z1), n*(z1 + z2 + y*z1*z2)], 
                                 [1/n * y, n*(1+y*z2)])
        pass

s_imped_th = SeriesImpedance(z=4+0.38j)
import numpy as np

class Network:
    def __init__(self, v1=None, v2=None, i1=None, i2=None, resultant_mtrx = None):
        self.resultant_mtrx = resultant_mtrx
        self.tensions = [v1, v2]
        self.currents = [i1, i2]
        pass
    
    def parallel_connection(self, matA, matB):
        A = np.dot(matA[0], matB[0][::-1])/(matA[0][1] + matB[0][1])
        B = (matA[0][1]*matB[0][1])/(matA[0][1] + matB[0][1])
        C = matA[1][0] + matA[1][0] + 1/((matA[0][1] + matB[0][1])) * (matA[0][0]-matB[0][0])
        D = np.dot(matA[:,1], matB[::-1, 1])/(matA[0][1] + matB[0][1])
        
        return np.array([[A, B],
                        [C, D]])

    def cascade_connection(self, *args):
    
        if len(args) < 2:
            raise ValueError('This function needs at least 2 arguments')
            
        result = np.dot(args[0],args[1])
        for i in range(2, len(args)):
                result = np.dot(result, args[i])
                
        return result
    
    def set_resultant_matrix(self, result):
        self.resultant_mtrx = result
        
    def set_tension1(self):
        try:
            self.tensions[0] = self.resultant_mtrx[0][0]*self.tensions[1] + self.resultant_mtrx[0][1]*self.currents[1]
        except TypeError:
                raise ValueError('Missing data!')
             
    def set_tension2(self):
        try:
            self.tensions[1] = (self.tensions[0] - self.resultant_mtrx[0][1]*self.currents[1])/self.resultant_mtrx[0][0]
        except TypeError:
            try:
                self.tensions[1] = (self.currents[0] - self.resultant_mtrx[1][1]*self.currents[1])/self.resultant_mtrx[1][0]
            except TypeError:
                raise ValueError('Missing data!')
            
    def set_current1(self):
        try:
            self.currents[0] = self.resultant_mtrx[1][0]*self.tensions[1] + self.resultant_mtrx[1][1]*self.currents[1]
        except TypeError:
                raise ValueError('Missing data!')
    
    def set_current2(self):
        try:
            self.currents[1] = (self.current[0] - self.resultant_mtrx[1][0]*self.tensions[1])/self.resultant_mtrx[1][1]
        except TypeError:
            try:
                self.currents[1] = (self.tensions[0] - self.resultant_mtrx[0][0]*self.tensions[1])/self.resultant_mtrx[0][1]
            except TypeError:
                raise ValueError('Missing data!')

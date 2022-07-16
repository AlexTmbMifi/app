# создал базис 
import numpy as np
import my_factorial as fl
class Basis:
    def __init__(self,m):
        self.m = m
    def Basis1(self):
        Z = np.eye(self.m)
        B= np.fliplr(Z)
        return B

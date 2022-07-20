import numpy as np
def Basis(m):
        Z = np.eye(m)
        B = np.fliplr(Z)
        return B
# создал базис 
import numpy as np
import my_factorial as fl
class Basis:
    def __init__(self,m,nmax,N):
        self.m = m
        self.nmax = nmax
        self.N = N
    # I wanna reduce my methods   
    # too many import as I could understand 
    def Basis1(self):
        R = (self.nmax+1)**self.m
        #import numpy as np
        B = np.zeros((R,self.m))
        for i in range(0,R,1):
            a = i
            for j in range(self.m-1,-1,-1):
                B[i][j] = a % (self.nmax + 1)
                a = int(a/(self.nmax +1))
        return B
    
    def Basis2(self):
        #import my_factorial as fl
        R = int(fl.factorial(self.m + self.N - 1) / fl.factorial(self.N) / fl.factorial(self.m - 1))
        #import numpy as np
        B = np.zeros((R,self.m))
        B[0][self.m - 1] = self.N
        for i in range(1,R,1):
            B[i][:] = B[i-1][:]
            if B[i][self.m-1] > 0:
                B[i][self.m-1] -= 1
                B[i][self.m-2] += 1
            else:
                k = self.m-1
                while k > 0:
                    k = k - 1
                    if B[i][k] > 0:
                        break
                B[i][self.m-1] = B[i][k] - 1
                B[i][k] = 0
                B[i][k-1] += 1
        return B
    
    def Basis3(self):
        #import my_factorial as fl
        b1 = self.Basis2() # вызов своей функции внутри одного класса. Без self вызывается внешняя функция
        #print(b1)
        R1 = int(fl.factorial(self.m + self.N - 1) / fl.factorial(self.N) / fl.factorial(self.m - 1))
        aR = 0
        for i in range(R1):
            for j in range(self.m-1):
                    if b1[i][j] > self.nmax:
                        j = self.m - 1
                        b1[i][1] = self.nmax + 1
                        aR = aR + 1
        R = R1 - aR
        #print(R1)
        #import numpy as np
        B = np.zeros((R,self.m))
        #print(B)
        j = 0
        for i in range(R1):
            if b1[i][0] <= self.nmax:
                    B[j][:] = b1[i][:]
                    j = j + 1
        return B


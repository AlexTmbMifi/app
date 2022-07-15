
class Hubbard:
    def __init__(self,N):
        self.N = N # размер сетки
    def neighbours(self,sick):
            sum4 = 0
            for j in range(len(sick)):
                #print(len(sick))
                nb = []
                rubbish = sick[:]# копирование
                #print(rubbish[0])
                rubbish[0] += 1
                if rubbish[0] <= self.N-1:
                    nb.append(rubbish)
                else:
                    rubbish[0] = 0
                    nb.append(rubbish)
                    

                rubbish = sick[:]
                rubbish[0] -= 1
                if rubbish[0] >= 0:
                    nb.append(rubbish)
                else:
                    rubbish[0] = self.N-1
                    nb.append(rubbish)
                    

                rubbish = sick[:]
                rubbish[1] += 1
                if rubbish[1] <= self.N-1:
                    nb.append(rubbish)
                else:
                    rubbish[1] = 0
                    nb.append(rubbish)

                rubbish = sick[:]
                rubbish[1] -= 1
                if rubbish[1] >= 0:
                    nb.append(rubbish)
                else:
                    rubbish[1] = self.N-1
                    nb.append(rubbish)
                
            return nb
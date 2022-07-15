
def CompareStrings(str,B):
        number = 0
        m = len(B[0,:]) 
        n = len(B[:,0]) 
        for i in range(m):
            count = 0
            for j in range(n):
                if B[i][j] == str[j]:
                    count += 1
                if count == n:
                    number = i
        return number
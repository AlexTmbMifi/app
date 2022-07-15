# расчёт факториал 
def factorial(P):
        factor = 1
        for i in range(2,P+1,1):
            factor *= i
        return factor
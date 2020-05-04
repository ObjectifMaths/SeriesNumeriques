from math import factorial

def Somme(n):
    S=0
    for k in range(n+1):
        S+=k**10000/factorial(k)
    return S



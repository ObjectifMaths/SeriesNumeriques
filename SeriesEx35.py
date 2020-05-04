import math

def Somme(n):
    S=0
    for k in range(0,n+1):
        S+=1/(3*k+2)/(3*k+4)
    return S

s=1/2-math.pi/6/math.sqrt(3)


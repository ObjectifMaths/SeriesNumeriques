from math import exp
def Somme(n):
    """calcul de la somme partielle d'ordre n
 de la série de terme général exp(n)/n!"""
    S,f=0,1
    for k in range(0,n+1):
        S+=exp(k)/f
        f*=(k+1)  # maintenant f contient (k+1)! 
    return S

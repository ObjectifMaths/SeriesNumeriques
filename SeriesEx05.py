from math import sqrt
def somme(e):
    #calcul du rang n pour que R_n <e
    n=int(1/e**2)
    #calcul de la somme partielle d'ordre n
    S,signe=0,1
    for k in range(1,n+1):
        S+=signe/sqrt(k)
        signe*=-1
    return S
    

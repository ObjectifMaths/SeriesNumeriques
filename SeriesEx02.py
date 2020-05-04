def Somme(n):
    """calcul de la somme partielle d'ordre n
 de la série de terme général (n+1)/n!"""
    S,f=0,1
    for k in range(1,n+2):
        S+=k/f
        f*=k
    return S

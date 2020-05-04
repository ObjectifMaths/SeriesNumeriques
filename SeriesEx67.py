from math import log, ceil
def Somme(err):
    """Calcul, avec une erreur maximale err, de 
$\sum\limits_{n=1}^\infty (\frac {n}{n+1})^{n^2} $"""
    # le reste est inférieur à 1/2^n
    n=ceil(-log(err)/log(2)) 
    S=0
    for k in range(1,n+1):
        S+=(k/(k+1))**(k**2)
    return S

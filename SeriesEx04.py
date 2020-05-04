from fractions import Fraction
def Somme(n):
    """calcul de la somme partielle d'ordre n
 de la série de terme général 1/((n+1)(n+2)(n+3))"""
    S1=S2=0
    for k in range(0,n+1):
        S1+=1/(k+1)/(k+2)/(k+3)
        S2+=Fraction(1, (k+1)*(k+2)*(k+3))
    return S1,S2



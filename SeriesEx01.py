"""Calcul des sommes partielles de la série de terme général $u_n=\frac{n}{(n+1)(n+2)}$"""


from fractions import Fraction

# avec des calculs exatcs sur les rationnels
def Somme1(n):
    S=0
    for k in range(0,n+1):
        S+=Fraction(k,(k+1)*(k+2))
    return S

# variante
def Somme2(n):
    return sum([Fraction(k,(k+1)*(k+2)) for k in range(1,n+1)])

# calculs approchés avec des flottants
def Somme3(n):
    S=0
    for k in range(0,n+1):
        S+=k/(k+1)/(k+2)
    return S
    


# représentation graphique
import matplotlib.pyplot as plt
import numpy as np
import os

X=np.arange(1,10000,10)
Y=np.array([Somme3(x) for x in X])
plt.plot(X,Y,color=(.8,.8,.2), linestyle=':', label=r"$S_n$")

# il semble que $S_n\sim \ln n$, tout comme $\sum_{k=1}^n \frac 1k$
plt.plot(X,np.log(X), 'r-',label=r"$x\mapsto ln x$")


plt.title(r"$S_n=\sum_{k=0}^n  \frac{k}{(k+1)(k+2)}$",fontsize=12)
plt.legend()
plt.grid()

FichierCourant=os.path.basename(__file__)
plt.savefig(FichierCourant[:-2]+"pdf")



 

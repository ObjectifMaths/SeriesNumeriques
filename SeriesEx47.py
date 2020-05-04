def Somme(n):
    S=0
    sf=1 # sum(p!, p, 0,k)
    f=1  # k!
    F=2  # (k+2)!
    for k in range(0,n+1):
        S+=sf/F
        f*=k+1
        sf+=f
        F*=(k+3)
    return S

from scipy.integrate import quad 
from scipy import exp,log
f=lambda u: -exp(u)*log(u)
s=quad(f,0,1)
print(s)

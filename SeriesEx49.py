from math import cos, sin, log, pi

def Sommes(N=10**6):
    """calcule les sommes partielles des séries
 $\sum\limits_{n=1}^\infty \frac{\sin n}{n}$
et 
$\sum\limits_{n=1}^\infty \frac{\cos n}{n}$

dont les sommes sont en théorie respectivement égales à $\frac{\pi-1}{2}$ et $-\ln\left(2\sin \frac 12\right) ?? 

"""
    S=C=0
    for n in range(1,N+1):
        C+=cos(n)/n
        S+=sin(n)/n
    Cinf = -log(2*sin(1/2))
    Sinf=(pi-1)/2
    return C, Cinf ,  S, Sinf


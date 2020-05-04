def Somme(n):
    S, signe, f = 0, 1, 1
    for k in range(0,n+1):
        S+= signe * k**3 / f
        signe*=-1
        f*=k+1 
    return S

    

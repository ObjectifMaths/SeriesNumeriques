def Somme(n):
    u=1 # u_1
    S=0
    for k in range(1:n+1):
        S+=u
        u*= (k/(k+1))**k # u_{k+1}
    return S



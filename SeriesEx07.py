import matplotlib.pyplot as plt
import numpy as np

f=lambda x: 1/x/np.log(x)

def Somme(n):
    L=[f(2)]
    for k in range(3,n):
        L.append(L[-1]+f(k))
    return np.array(L)

n=1000
X=np.arange(2,n)
Y=Somme(n)

plt.plot(X,Y,color=(.7,.2,.9),linestyle=':',label=r"$S_n$")
plt.plot(X,np.log(np.log(X+1)-np.log(np.log(2))),'r-', label=r"$x\mapsto \mathrm{ln} \mathrm{ln}(x+1)-\mathrm{ln} \mathrm{ln}(2)$")

plt.legend()
plt.grid()
plt.savefig("SeriesEx07.pdf")

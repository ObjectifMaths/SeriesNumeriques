import matplotlib.pyplot as plt
import numpy as np

n=10

X=np.arange(0,n)
S=[1]
u=1
for i in range(1,n):
    u*=(-1/3)
    S.append(S[-1]+u)
Y=np.array(S)

plt.plot(X,Y,'bo', label="Sommes partielles")
plt.plot([0,n],[3/4,3/4], 'r-',label="Somme")
plt.grid()
plt.legend()
plt.savefig("SeriesEx18.pdf")

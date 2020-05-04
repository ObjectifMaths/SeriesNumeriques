def devdec(p,q):
    """calcule le développement décimal de p/q
13/14 = 0.9 285714 285714 286...
devdec(13,14)
>>> ([0, 9], [2, 8, 5, 7, 1, 4])"""
    e, p=p//q , p%q
    D, R=[], []
    while p not in R:
        R.append(p)
        D.append(10*p//q)
        p=10*p%q
    i=R.index(p)
    return [e]+D[:i ], D[i:]

def PeriodeMax(q):
    """détermine la longueur de la plus grand période
 pour un rationnel de dénominateur q"""
    M=0
    for p in range(1,q):
        D=devdec(p,q)
        M=max(M,len(D[1]))
    return M

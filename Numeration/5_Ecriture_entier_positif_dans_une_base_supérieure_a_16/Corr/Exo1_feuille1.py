def convertir(n, base=2):

    if n == 0:
        return(n)

    resultat = []
    reste = n
    while n >= 1:
        reste = n%2
        n = n//2
        resultat.append(reste)
    print(resultat)
    r=""    #resultat = resultat[::-1]
    for i in range(len(resultat)-1,-1,-1):
        r=r+str(resultat[i])
    return(r)

print(convertir(13))
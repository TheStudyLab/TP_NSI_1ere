def recherche_indice(e, l):
    i = 0
    continuer = True
    while i < len(l) and continuer:
        if l[i] == e:
            continuer = False
        else:
            i += 1
    return(e,i)
L = [45, 21, 56, 1, 7, 32, 25, 7, 44]
a,b = recherche_indice(25,L)
print("La première occurence de", a, "est à l'indice", b)

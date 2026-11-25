def recherche_i(e, l):
    if len(l) == 0:
        return "La liste est vide."
    indice = -1
    continuer = True
    for i in range(len(l)):
        if l[i] == e and continuer:
            indice = i
            continuer = False
    if indice == -1:
        return "L'occurence n'existe pas."
    return("L'élément :", e, "est à l'indice :", indice)

print("_______for_______")
L = [45, 21, 56, 1, 7, 32, 25, 7, 44]
print(recherche_i(21,L))
print(recherche_i(21,[]))
print(recherche_i(0,L))

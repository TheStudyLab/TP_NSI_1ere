l = [4, 48, 3, 9, 4, 48, 7, 4, 3]

def moyenne_for(l):
    if len(l) == 0:
        return None

    somme = 0
    for number in l:
        somme += number
    return somme / len(l)

print("Moyenne de la liste l (methode for) : ", moyenne_for(l))

def moyenne_while(l):
    if len(l) == 0:
        return None

    somme = 0
    i = 0
    while i < len(l):
        somme += l[i]
        i += 1
    return somme / len(l)

print("Moyenne de la liste l (methode while) : ", moyenne_while(l))
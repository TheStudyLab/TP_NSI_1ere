l = [4, 48, 3, 9, 4, 48, 7, 4, 3]

# question 1. a)

def nb_occurences_1_for(e,l):
    cpt = 0
    for i in l:
        if i == e:
            cpt += 1
    return cpt

print("Nombre d'occurrences de 4 dans la liste l (méthode for) : ", nb_occurences_1_for(4,l))

def nb_occurences_1_while(e,l):
    cpt1 = 0
    i = 0
    while i < len(l):
        if l[i] == e:
            cpt1 += 1
        i += 1
    return cpt1

print("Nombre d'occurrences de 4 dans la liste l (méthode while) : ", nb_occurences_1_while(4,l))

# question 1. b)

def nb_occurences_2_count(e,l):
    return l.count(e)

print("Nombre d'occurrences de 4 dans la liste l (méthode count) : ", nb_occurences_2_count(4,l))
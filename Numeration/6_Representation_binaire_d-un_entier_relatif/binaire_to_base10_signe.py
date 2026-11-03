binaire = [1, 0, 1, 1, 1, 0, 1, 0]

nb_saisi = list(binaire)
signe = binaire[0]

if signe == 1:
    complement_a_1 = []
    for bit in binaire:
        if bit == 1:
            complement_a_1.append(0)
        else:
            complement_a_1.append(1)

    complement_a_2 = list(complement_a_1)
    retenue = 1

    for i in range(len(complement_a_2) - 1, -1, -1):
        somme = complement_a_2[i] + retenue
        complement_a_2[i] = somme % 2
        retenue = somme // 2

    valeur_absolue = 0
    taille = len(complement_a_2)
    for i in range(taille):
        puissance = taille - 1 - i
        valeur_absolue = valeur_absolue + complement_a_2[i] * (2 ** puissance)

    valeur_decimale = -valeur_absolue

else:
    
    complement_a_2 = list(binaire)
    valeur_absolue = 0
    taille = len(binaire)
    for i in range(taille):
        puissance = taille - 1 - i
        valeur_absolue = valeur_absolue + binaire[i] * (2 ** puissance)

    valeur_decimale = valeur_absolue

print("nb saisi (liste) avant le test du signe : ", nb_saisi)
print("Sa représentation en complément à 2 est :  ", complement_a_2)
print("Le signe signe au départ est :  ", signe)
print("L'écriture décimale de ce nombre est : - ", abs(valeur_decimale) if valeur_decimale < 0 else valeur_decimale)
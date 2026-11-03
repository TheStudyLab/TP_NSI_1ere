def complement_a_deux(nb):
    inverse = [1 - bit for bit in nb]
    print("Complément à 1 : ", inverse)
    
    retenue = 1
    resultat = list(inverse)
    
    for i in range(len(resultat) - 1, -1, -1):
        somme = resultat[i] + retenue
        if somme == 2:
            resultat[i] = 0
            retenue = 1
        else:
            resultat[i] = somme
            retenue = 0
            
    return resultat


nb1 = [0, 0, 1, 0]
print("nb saisi (liste) avant le test du signe :", nb1)
print("Sa représentation en complément à 2 est :", complement_a_deux(nb1))

print("-" * 50)

nb2 = [1, 0, 1, 1, 1, 0, 1, 0]
print("nb saisi (liste) avant le test du signe :", nb2)
print("Sa représentation en complément à 2 est :", complement_a_deux(nb2))
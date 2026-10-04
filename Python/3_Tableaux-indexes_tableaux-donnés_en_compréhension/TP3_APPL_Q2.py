L = [3, 5, 7, 5, 9, 3, 5, 3]

occu_5 = L.count(5)
print("Le nombre d'occurrences de 5 dans la liste L est :", occu_5)

indices_5 = [index for index, value in enumerate(L) if value == 5]
print("Les indices des occurrences de 5 dans la liste L sont :", indices_5)

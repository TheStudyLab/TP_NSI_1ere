L = [1, 2, 7, 12, 14, 21, 34, 72]

# Méthode 1 : Parcours par indice
print("----Méthode 1 : Parcours par indice----"+"\n")

L3 = []
for i in range(len(L)):
    if L[i] % 3 == 0:
        L3.append(L[i])

print("(L3) Les nombres divisibles par 3 dans la liste L sont :", L3)
print("\n")

# Méthode 2 : Parcours par élément
print("----Méthode 2 : Parcours par élément----"+"\n")

L33 = []
for element in L:
    if element % 3 == 0:
        L33.append(element)

print("(L33) Les nombres divisibles par 3 dans la liste L sont :", L33)
print("\n")

# Méthode 3 : Compréhension de liste
print("----Méthode 3 : Compréhension de liste----"+"\n")

L333 = [element for element in L if element % 3 == 0]

print("(L333) Les nombres divisibles par 3 dans la liste L sont :", L333)
print("\n")
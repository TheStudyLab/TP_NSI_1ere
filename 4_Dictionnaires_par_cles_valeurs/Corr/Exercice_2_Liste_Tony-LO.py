#Exercice 2#

L = [3, 5, 7, 5, 9, 3, 5, 3]

cpt=0

element=5
index=[]
for i in range(len(L)):
    if L[i] == element:
        index.append(i)
        cpt=cpt+1

print("Le nombre d'occurences de", element, "dans", L, "est", cpt, "et apparaît aux index", index)

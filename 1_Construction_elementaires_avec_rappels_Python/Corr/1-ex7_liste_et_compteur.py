# 1-ex7
liste_animaux=["lapin","chat","chien","chiot","lapin","dragon","loup"]
c=0
for animal in liste_animaux :  # parcours par élément
    print(animal)
    if animal=="lapin":
        c=c+1
print ("c ",c)

print ("----------------------------")

cp=0
for i in range(len(liste_animaux)) : # parcours par indice (ou index), i est cet indice
    print(liste_animaux[i])
    if liste_animaux[i]=="lapin":
        cp=cp+1
print ("cp ",cp)














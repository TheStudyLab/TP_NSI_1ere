liste_animaux = ["lapin","chat","chien","chiot","dragon","loup","lapin"]

cpt1 = 0
cpt2 = 0
cpt_lapin1 = 0
cpt_lapin2 = 0

for animal in liste_animaux :
    cpt1 += 1
    print(str(cpt1) + ". " + animal)
    if animal == "lapin" :
        cpt_lapin1 = cpt_lapin1 + 1
        print("--> Nouveau nbs de lapin dans la liste :",cpt_lapin1)
    
print("\n")

for i in range (len(liste_animaux)):
    cpt2 += 1
    print(str(cpt2) + ". " + liste_animaux[i])
    if liste_animaux[i] == "lapin":
        cpt_lapin2 = cpt_lapin2 + 1
        print("--> Nouveau nbs de lapin dans la liste :",cpt_lapin2)

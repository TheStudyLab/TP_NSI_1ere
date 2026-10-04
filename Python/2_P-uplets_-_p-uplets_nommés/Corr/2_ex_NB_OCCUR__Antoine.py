prenom=input("Saisir un prénom de la liste:")
occurence=0

eleve1=("Geoffroy","Blas",1)
eleve2=("Yann","Delarue",2)
eleve3=("Noé","Fèvre",1)
eleve4=("Thomas","Marchand",2)
eleve5=("Noé","Durant",1)
eleve6=("Noé","Guyon",2)
eleve7=("Sacha","Tuile",1)
eleve8=("Nathan","Valko",2)
classe=(eleve1,eleve2,eleve3,eleve4,eleve5,eleve6,eleve7,eleve8)

for e in classe:                # parcours par élément
   if e[0] == prenom:
        occurence = occurence + 1

if occurence > 0:
    print (f"Le nombre d'occurences de {prenom} est {occurence}")
else:
    print(f"Il n'y a aucune personne qui porte le nom {prenom} dans cette classe.")

for i in range (len(classe)):   # parcours par indice
   if classe[i][0] == prenom:
        occurence = occurence + 1





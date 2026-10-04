prenom=input("Saisir un prénom de la liste : ")

eleve1=("Geoffroy","Blas",1)
eleve2=("Yann","Delarue",2)
eleve3=("Noé","Fèvre",1)
eleve4=("Thomas","Marchand",2)
eleve5=("Noé","Durant",1)
eleve6=("Noé","Guyon",2)
eleve7=("Sacha","Tuile",1)
eleve8=("Nathan","Valko",2)
classe=(eleve1, eleve2 ,eleve3 ,eleve4 ,eleve5 ,eleve6 ,eleve7 ,eleve8)

# 1 Afficher le nombre d'occurences du prénom saisi
# 2 Afficher le nombre d'occurences seulement s'il est supérieur ou égal à 2
# sinon dire qu'il n'est pas présent plus d'une fois

nb_occu = 0
nb_occu2 = 0
#for i in range(len(classe)):
#    print(f"i: {i} classe[i] : {classe[i]}   _   classe[i][0] : {classe[i][0]}")

for i in range (len(classe)):
    if classe [i][0] == prenom : 
        nb_occu = nb_occu + 1
        
if nb_occu >= 2 :
    print(f"Ce prémon est répété {nb_occu} dans la liste")
else :
    print("Ce prénom n'est pas présent plus d'uwpne fois dans la liste")

print("--------------------")

for e in classe :
    if e[0] == prenom:
        nb_occu2 = nb_occu2 + 1

if nb_occu2 >= 2 :
    print(f"Ce prémon est répété {nb_occu2} dans la liste")
else :
    print("Ce prénom n'est pas présent plus d'une fois dans la liste")

djardin= {
'jaune':['citron','banane','pomme'],
'vert':['kiwi','pomme'],
'rouge':['fraise','cerise','framboise','groseille','pomme'],
'violet':['aubergine']
}

for couleur,liste in djardin.items():
    for i in liste:
        if i == 'pomme':
            print("La pomme est",couleur)

print("\n ---------------------------------- \n")

for couleur,liste in djardin.items():
    for i in range(len(liste)):
        if liste[i] == 'pomme':
            print("La pomme est",couleur)

print("\n ---------------------------------- \n")

for couleur in djardin:
    for i in range(len(djardin[couleur])):
        if djardin[couleur][i] == 'pomme':
            print("La pomme est",couleur)

print("\n ---------------------------------- \n")

for couleur in djardin:
    for e in djardin[couleur]:
        if e == 'pomme':
            print("La pomme est",couleur)














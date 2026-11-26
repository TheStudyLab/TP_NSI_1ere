L = [3,4.5,"a",("z",6),[],[4,"d"],{"chien":4,"chat":5}]

print(type(L[1]))
print(type(L[3]))
print(type(L[6]))

print("\n")
print("-------------PARCOURS ET LISTES------------")
print("\n")


maListe = ['lundi', 'mardi', 'mercredi', 'jeudi']

print(maListe)

for i in range(len(maListe)):
    print(maListe[i], end=" ")

print("\n-------------")

for e in maListe:
    print(e, end=" ")


print("\n")
print("-------------COPIES DE LISTES------------")
print("\n")

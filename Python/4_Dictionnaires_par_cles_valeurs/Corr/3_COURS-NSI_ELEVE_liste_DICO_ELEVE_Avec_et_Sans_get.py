d={'courgette': 'vert', 'myrtille': 'violet', 'cerise': 'rouge',
'carotte': 'orange', 'citron': ['jaune', 'vert']}
print(d)

supp_myrtille=d.pop("myrtille")
print("suppression de 'myrtille' : ",supp_myrtille)

print(d["citron"]," ",type(d["citron"]))

print(d["citron"][1]," ",type(d["citron"][1]))

d["citron"].pop()
print(d)

print("---- Avec la méthode get() ---")

texte = "exemple de texte"
d = {}
for caractere in texte:
    d[caractere] = d.get(caractere, 0) + 1
print(d)
# {'e': 5, 'x': 1, 'a': 1, 'm': 1, 'p': 1, 'l': 1, ' ': 2, 'd': 1, 't': 2}

print("\n---- Sans la méthode get() ---")

dico = {}                        # Initialisation du dictionnaire dico
for c in texte:                  # On parcourt les caractères du texte
    if c in dico:                  # On vérifie si la clé c est dans dico (ou bien : if c in dico.keys():)
        dico[c] += 1             # On ajoute 1 à la valeur de la clé c
    else:
        dico[c] = 1              # le caractère n'existe pas dans dico, on le crée
print(dico)
# {'e': 5, 'x': 1, 'a': 1, 'm': 1, 'p': 1, 'l': 1, ' ': 2, 'd': 1, 't': 2}

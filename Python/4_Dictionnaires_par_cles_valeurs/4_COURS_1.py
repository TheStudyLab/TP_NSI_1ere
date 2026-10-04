print("=== 1. Qu'est-ce qu'un dictionnaire ===\n")

print("1.1 Différences entre une liste et un dictionnaire\n")

L = ["a", "b"]  # Avec une liste
                # L[0] = "a"
                # L[1] = "b"
print(L)

dico = {"cle1": "a", "cle2": "b"}   # Avec un dictionnaire
                                    # dico["cle1"] = "a"
                                    # dico["cle2"] = "b"
print(dico)

print("\n=== 2. Utilisation d'un dictionnaire ===\n")

print("2.1 Comment créer un dico\n")

jardin ={"courgette":"vert",    # clé : courgette, valeur : vert
         "myrtille":"violet",   # clé : myrtille, valeur : violet
         "cerise":"rouge",      # clé : cerise, valeur : rouge
         "carotte":"orange"}    # clé : carotte, valeur : orange
print(jardin)

print("\n2.2 Comment ajouter des valeurs\n")

jardin["aubergine"] = "mauve" # clé : aubergine, valeur : mauve
print(jardin)

jardin["citron"] = "jaune", "vert" # clé : citron, valeur : ('jaune', 'vert')
print(jardin)

print("\n2.3 Comment supprimer des valeurs\n")

print("--- Méthode 1 ---")
del jardin["aubergine"] # clé : aubergine, valeur : mauve
print(jardin)

print("--- Méthode 2 ---")
supp_mirtille = jardin.pop("myrtille") # clé : myrtille, valeur : violet
print("supprimé :", supp_mirtille)     # affiche : supprimé : violet
print(jardin)

print("\n2.4 Tester la présence d'une clé\n")

if "citron" in jardin.keys():                       # On vérifie si la clé "citron" est dans les clés du dictionnaire
    print("il y a des citropns dans le jardin")     # affiche : il y a des citrons dans le jardin
else:
    print("il n'y a pas de citrons dans le jardin") # affiche : il n'y a pas de citrons dans le jardin

print("\n2.5 Tester la présence d'une valeur\n")

if "rouge" in jardin.values():                      # On vérifie si la valeur "rouge" est dans les valeurs du dictionnaire
    print("il y a des cerises dans le jardin")      # affiche : il y a des cerises dans le jardin
else:
    print("il n'y a pas de cerises dans le jardin") # affiche : il n'y a pas de cerises dans le jardin

jardin["citron"] = "jaune","vert"                   # clé : citron, valeur : ('jaune', 'vert')

if "jaune" in jardin.values():                      # On vérifie si la valeur "jaune" est dans les valeurs du dictionnaire
    print("il y a des citrons dans le jardin")      # affiche : il y a des citrons dans le jardin
else:
    print("il n'y a pas de citrons dans le jardin") # affiche : il n'y a pas de citrons dans le jardin

print("\n2.6 Accéder aux éléments d'un dictionnaire\n")

print(jardin["citron"])                 #('jaune', 'vert')
print(jardin.get("courgette"))          # vert

print(jardin.get("pomme"))              # None

print("\n2.7 Connaitre le nombre de couples clé/valeur d'un dictionnaire\n")

len(jardin)                                                     #affiche : 4
print("Le dictionnaire contient", len(jardin), "éléments")      # affiche : Le dictionnaire contient 4 éléments

print("\n=== 3. Les méthodes de parcours ===\n")

print("3.1 Parcourir les clés d'un dictionnaire\n")

for element in jardin.keys():               # On parcourt les clés du dictionnaire
    print(element, end=" ") # courgette
                            # cerise
                            # carotte
                            # citron

print("\n")
print("3.2 Parcourir les valeurs d'un dictionnaire\n")

for couleur in jardin.values():             # On parcourt les valeurs du dictionnaire
    print(couleur, end=" ") # vert
                            # rouge
                            # orange
                            # ('jaune', 'vert')

print("\n")
print("3.3 Parcourir les couples clé/valeur d'un dictionnaire (simultanés)\n")

for element, couleur in jardin.items():     # On parcourt les couples clé/valeur du dictionnaire
    print(element, ":", couleur) # courgette : vert
                                 # cerise : rouge
                                 # carotte : orange
                                 # citron : ('jaune', 'vert')

print("\n3.4 Compter les caractères d'un texte\n")

print("---- Avec la méthode get() ---\n")

texte = "exemple de texte"
d = {}                                 # Initialisation du dictionnaire
for cpt in texte:                      # On parcourt les caractères du texte
    d[cpt] = d.get(cpt, 0) + 1         # On ajoute 1 à la valeur de la clé cpt, si elle n'existe pas on l'initialise à 0
print(d) # {'e': 5, 'x': 1, 'a': 1, 'm': 1, 'p': 1, 'l': 1, ' ': 2, 'd': 1, 't': 2}

print("---- Sans la méthode get() ---\n")

d2 = {}                                # Initialisation du dictionnaire
for cpt in texte:                      # On parcourt les caractères du texte
    if cpt in d2:                      # On vérifie si la clé cpt est dans le dictionnaire
        d2[cpt] += 1                   # On ajoute 1 à la valeur de la clé cpt
    else:           
        d2[cpt] = 1                    # On initialise la valeur de la clé cpt à 1
print(d2) # {'e': 5, 'x': 1, 'a': 1, 'm': 1, 'p': 1, 'l': 1, ' ': 2, 'd': 1, 't': 2}

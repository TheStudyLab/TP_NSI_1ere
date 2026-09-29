# Exercice 3

personne = {"nom": "Delaruelle", "prenom": "Karl", "age": 22, "tel": "0612345678", "email": "dk@exple.fr"}

print("1. Clés du dictionnaire :\n")

for cle in personne.keys():           # Parcourt chaque clé dans le dictionnaire
    print(cle)                        # Affiche la clé actuelle

print("\n2. Valeurs du dictionnaire :\n")

for valeur in personne.values():      # Parcourt chaque valeur dans le dictionnaire
    print(valeur)                     # Affiche la valeur actuelle

print("\n3. Clés et valeurs du dictionnaire :\n")

for cle, valeur in personne.items():  # Parcourt chaque paire clé-valeur dans le dictionnaire
    print(f"{cle} : {valeur}")        # Affiche la clé et la valeur actuelles
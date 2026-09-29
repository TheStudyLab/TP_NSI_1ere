# Exercice 1

dicojardin = {'jaune':'banane','vert':'kiwi','rouge':'fraise'}

print("« De quelle couleur est la banane ? »\n")

if 'jaune' in dicojardin:                # Vérifie si la clé 'jaune' est dans le dictionnaire
    print("La banane est jaune")         # Affiche un message si la banane est jaune
else:                                    # Si la clé 'jaune' n'est pas dans le dictionnaire
    print("La banane n'est pas jaune")   # Affiche un message si la banane n'est pas jaune

print("\n« Quel est le fruit de couleur verte ?  »\n")

for cle, valeur in dicojardin.items():                              # Parcourt chaque paire clé-valeur dans le dictionnaire
    if cle == 'vert':                                               # Vérifie si la cle est 'vert'
        print(f"Le fruit de couleur verte est le {valeur}")         # Affiche le fruit de couleur verte                                                         # Sort de la boucle après avoir trouvé le fruit vert
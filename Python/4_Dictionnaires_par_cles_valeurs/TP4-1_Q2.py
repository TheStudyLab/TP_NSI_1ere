# Exercice 2

dicojardin = {
    'jaune':    ['citron', 'banane', 'pomme'],
    'vert':     ['kiwi', 'pomme'],
    'rouge':    ['fraise', 'cerise', 'framboise', 'groseille', 'pomme'],
    'violet':   ['aubergine']
}

print("« De quelle couleur est la pomme ? »\n")

for couleur, fruits in dicojardin.items():      # Parcourt chaque paire clé-valeur dans le dictionnaire
    if 'pomme' in fruits:                       # Vérifie si 'pomme' est dans la liste des fruits pour la couleur actuelle
        print(f"La pomme est {couleur}")        # Affiche la couleur de la pomme si elle est trouvée dans la liste des fruits
    else:                                       # Si 'pomme' n'est pas dans la liste des fruits pour la couleur actuelle
        print(f"La pomme n'est pas {couleur}")

print("\n« Combien y-a-t-il de fruits rouges ?  »\n")

print(f"Il y a {len(dicojardin['rouge'])} fruits rouges dans le dictionnaire.") # Affiche le nombre de fruits rouges dans le dictionnaire

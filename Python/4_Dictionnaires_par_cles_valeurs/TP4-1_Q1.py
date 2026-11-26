# Exercice 1

dicojardin = {'jaune':'banane','vert':'kiwi','rouge':'fraise'}

print("« De quelle couleur est la banane ? »\n")

for couleur, fruit in dicojardin.items():      
    if fruit == 'banane':                      
        print(f"La banane est {couleur}")      
        

print("\n--- Autre méthode : ---\n")

for cf in dicojardin.items():      
    if cf[1] == 'banane':                      
        print(f"La banane est {cf[0]}")
        

print("\n« Quel est le fruit de couleur verte ?  »\n")

for cle, valeur in dicojardin.items():                              
    if cle == 'vert':                                               
        print(f"Le fruit de couleur verte est le {valeur}")
        


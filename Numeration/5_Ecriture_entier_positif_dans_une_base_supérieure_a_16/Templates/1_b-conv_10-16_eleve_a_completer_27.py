# 1_b-conv_10-16
nombre = 458
n = nombre
# Les caractères utilisés en base 16
symboles = "0123456789ABCDEF"
# chaque valeur dans la liste 'symboles' correspond à sa position dans la liste
# exemple : symboles[10] = A et 10 en écriture décimale correspond à A en écriture hexadécimale
liste = []

# Étape 1 : récupérer les restes des divisions par 16
while n >= 1:
    ...




print("Liste des restes :", liste)

# Étape 2 : transformer chaque reste en caractère hexadécimal
l_hexa = []
...




print("Liste hexadécimale :", l_hexa)


# Étape 3 : lire les caractères dans l'ordre inverse
resul_b16 = ""

for j in range(len(l_hexa) - 1, -1, -1):
    ...



print("Résultat en base 16 :", resul_b16)

# Dans la console, vous obtenez :
# Liste des restes : [10, 12, 1]
# Liste hexadécimale : ['A', 'C', '1']
# Résultat en base 16 : 1CA

# --- Initialisation des variables ---

# On demande la valeur hexadécimale à l'utilisateur et on la passe en majuscules
# afin de gérer aussi bien les saisies comme "e9" que "E9"
entree = input("Entrez la valeur hexadécimale du caractère ISO 8859-15 : ").upper()

# Table des caractères hexadécimaux : l'indice de chaque caractère correspond à sa valeur en base 10
hexadecimal = "0123456789ABCDEF"

base10 = 0
base2 = ""
e = 0  # Exposant pour les puissances de 16

# --- Conversion de la base 16 (hexadécimal) vers la base 10 (décimal) ---

# On parcourt la chaîne de droite à gauche (du poids faible au poids fort)
for i in range(len(entree) - 1, -1, -1):
    # On cherche la valeur décimale associée au caractère courant
    for j in range(len(hexadecimal)):
        if entree[i] == hexadecimal[j]:
            # On ajoute chiffre * 16^exposant puis on incrémente l'exposant
            base10 += j * (16 ** e)
            e += 1

print(entree + " en base 10 vaut " + str(base10))

# --- Conversion de la base 10 (décimal) vers la base 2 (binaire) ---

# On utilise une copie 'n' pour conserver intacte la valeur de 'base10'
n = base10

if n == 0:
    base2 = "0"
else:
    # Méthode des divisions euclidiennes successives par 2
    while n > 0:
        base2 += str(n % 2)  # On récupère le reste (0 ou 1)
        n //= 2              # On effectue la division entière par 2
    # Les restes ont été collectés à l'envers : on inverse la chaîne
    base2 = base2[::-1]

print(entree + " en base 2 vaut " + base2)

# --- Encodage UTF-8 (1 octet ou 2 octets maximum) ---

if len(base2) <= 7:
    # Cas sur 1 octet : format 0xxxxxxx (7 bits utiles précédés d'un 0)
    padded = base2
    while len(padded) < 7:
        padded = "0" + padded  # Bourrage avec des zéros à gauche jusqu'à 7 bits
    utf8 = "0" + padded
    print(entree + " en UTF-8 vaut " + utf8)
else:
    # Cas sur 2 octets : format 110yyyyy 10xxxxxx (11 bits utiles au total)
    base2_11 = base2
    while len(base2_11) < 11:
        base2_11 = "0" + base2_11  # Bourrage avec des zéros à gauche jusqu'à 11 bits

    bits_gauche = base2_11[:-6]  # Les bits de poids fort (5 bits)
    bits_droite = base2_11[-6:]  # Les 6 bits de poids faible

    # On s'assure que la partie gauche comporte bien 5 bits
    padded_gauche = bits_gauche
    while len(padded_gauche) < 5:
        padded_gauche = "0" + padded_gauche

    octet_gauche = "110" + padded_gauche
    octet_droite = "10" + bits_droite

    print(entree + " en UTF-8 vaut " + octet_gauche + " " + octet_droite)

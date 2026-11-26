user = list(input("Entrez la valeur hexadecimale du caractere ISO 8859-15 : "))
res = []

# recuperation caracteres saisis (2 caracteres pour ISO 8859-15, ou plus : bonus)
for c in user:
    res.append(c)

# 1) conversion symbole hexadecimal en valeur decimale
for i in range(len(res)):
    caractere = res[i].upper()  # convertir en majuscule pour simplifier les tests
    
    if caractere == 'A':
        res.append('10')
    elif caractere == 'B':
        res.append('11')
    elif caractere == 'C':
        res.append('12')
    elif caractere == 'D':
        res.append('13')
    elif caractere == 'E':
        res.append('14')
    elif caractere == 'F':
        res.append('15')
    else:
        res.append(caractere)   # si chiffre entre 0 et 9, on ajoute directement sa valeur
        
print("resultat", res)

# 2) conversion base 16 en base 10
# les valeurs converties sont dans la seconde moitie de la liste res
valeurs = res[len(user):]
decimal = 0
puissance = len(valeurs) - 1

for val in valeurs:
    decimal += int(val) * (16 ** puissance)
    puissance -= 1

print("En ecriture decimale :", decimal)

# 3) conversion base 10 en base 2 (divisions successives par 2)
if decimal == 0:
    binaire = "0"
else:
    binaire = ""
    n = decimal
    while n > 0:
        reste = n % 2
        binaire = str(reste) + binaire
        n = n // 2

print("En base 10, la valeur est", decimal, "et en base 2 est :")
print(binaire)

# 4) generation codage UTF-8 a partir de ecriture binaire
nb_bits = len(binaire)

if nb_bits <= 7:
    # codage sur 1 octet : 0xxxxxxx
    zeros = "0" * (8 - nb_bits)
    utf8_detail = zeros + binaire
    utf8 = zeros + binaire

elif nb_bits <= 11:
    # codage sur 2 octets : 110yyyyy 10xxxxxx
    octet_droite = "10" + binaire[-6:]
    reste_gauche = binaire[:-6]
    zeros_gauche = "0" * (5 - len(reste_gauche))
    octet_gauche = "110" + zeros_gauche + reste_gauche
    
    utf8_detail = "110" + zeros_gauche + "_" + reste_gauche + " " + "10" + "_" + binaire[-6:]
    utf8 = octet_gauche + octet_droite

elif nb_bits <= 16:
    # bonus - codage sur 3 octets : 1110zzzz 10yyyyyy 10xxxxxx
    octet_droite = "10" + binaire[-6:]
    octet_milieu = "10" + binaire[-12:-6]
    reste_gauche = binaire[:-12]
    zeros_gauche = "0" * (4 - len(reste_gauche))
    octet_gauche = "1110" + zeros_gauche + reste_gauche
    
    utf8_detail = octet_gauche + "_" + octet_milieu + "_" + octet_droite
    utf8 = octet_gauche + octet_milieu + octet_droite

print("La valeur en utf-8 vaut", utf8_detail, "soit:")
print(utf8)
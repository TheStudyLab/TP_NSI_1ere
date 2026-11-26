# --- 1. Fonctions mathématiques et de comparaison ---

# abs(x) : valeur absolue d'un nombre (int, float ou complexe)
print("abs(-5) :", abs(-5))

# min(iterable) et max(iterable) : minimum et maximum d'un itérable non vide d'éléments comparables
L = [4, 7, 3, 12, 5, 17, 1, 19]
print("min(L) :", min(L))
print("max(L) :", max(L))

# pow(x, y) : x puissance y (x et y doivent être des nombres)
print("pow(2, 3) :", pow(2, 3))

# round(nombre, n) : arrondit un nombre à n chiffres après la virgule (n est un entier)
print("round(3.14159, 2) :", round(3.14159, 2))


# --- 2. Fonctions de conversion de types ---

# bool(x) : convertit en booléen (False pour 0, "", [], None ; True sinon)
print("bool(0) :", bool(0), "| bool(42) :", bool(42))

# int(x) : convertit un nombre ou une chaîne valide (sans décimale) en entier
print("int('15') :", int("15"), "| int(3.9) :", int(3.9))

# float(x) : convertit un nombre ou une chaîne valide (avec un point) en flottant
print("float('3.14') :", float("3.14"))

# str(x) : convertit n'importe quel objet en chaîne de caractères
print("str(123) :", str(123))

# list(iterable) : convertit un itérable en liste
print("list('ABC') :", list("ABC"))

# tuple(iterable) : convertit un itérable en tuple (non modifiable)
print("tuple([1, 2, 3]) :", tuple([1, 2, 3]))


# --- 3. Fonctions sur les séquences et caractères ---

# len(s) : longueur d'une séquence ou collection (ne fonctionne pas sur un nombre)
print("len(L) :", len(L))

# chr(i) : caractère associé au code Unicode entier i (0 <= i <= 1 114 111)
print("chr(65) :", chr(65))

# range(debut, fin, pas) : séquence d'entiers de debut à fin-1 (arguments entiers, pas != 0)
print("list(range(0, 10, 2)) :", list(range(0, 10, 2)))


# --- 4. Fonctions d'information, d'entrée et de sortie ---

# type(x) : renvoie le type de l'objet x
print("type(L) :", type(L))

# print(...) : affiche des objets dans la console
print("print() affiche ce message à l'écran.")

# input(invite) : met en pause et récupère la saisie clavier sous forme de str
# (Décommenter les 2 lignes ci-dessous pour tester)
# nom = input("Entrez votre prénom : ")
# print("Bonjour", nom)

# help(objet) : affiche la documentation intégrée d'un objet ou d'une fonction
# (Décommenter la ligne ci-dessous pour afficher l'aide de len)
# help(len)
dico_zoo = {'elephant': ('Asie', 5),
            'écureuil': ('Asie', 17),
            'panda': ('Asie', 2),
            'hippopotame': ('Afrique', 7),
            'girafe': ('Afrique', 4)}

# print("1. Nombre d'animaux originaires d'Asie :\n")

cpt = 0

for animal, (continent, nb) in dico_zoo.items():
    if continent == 'Asie':
        # print(f"{animal} : {nb}")
        cpt = cpt + nb
print(f"\nNombre d'animaux originaires d'Asie : {cpt}\n")


# print("\n2. Nom des animaux originaires d'Asie :\n")

l=[]

for animal, (continent, nb) in dico_zoo.items():
    if continent == 'Asie':
        l.append(animal)

print(f"Nom des animaux originaires d'Asie : {l}\n")


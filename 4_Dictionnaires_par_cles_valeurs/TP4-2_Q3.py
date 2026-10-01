animaux = [ {'nom':'Medor', 'espece':'chien', 'age':5, 'enclos':2},
            {'nom':'Titine', 'espece':'chat', 'age':2, 'enclos':5},
            {'nom':'Tom', 'espece':'chat', 'age':7, 'enclos':4},
            {'nom':'Belle', 'espece':'chien', 'age':6, 'enclos':3},
            {'nom':'Mirza', 'espece':'chat', 'age':6, 'enclos':5}]

num_enclos = int(input("Entrez le numéro de l'enclos : "))

animaux_par_enclos = []

for animal in animaux:
    if animal['enclos'] == num_enclos:
        animaux_par_enclos.append(animal)
print(f"num_enclos = {num_enclos}")
print(animaux_par_enclos)
        





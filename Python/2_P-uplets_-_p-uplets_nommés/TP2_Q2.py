note = (12, 15, 9, 18)

# essayaie de modifier la premiere note du tuple
# note[0] = 5
# IMPOSSIBLE --> Renvoi d'une erreur : 
# "TypeError: 'tuple' object does not support item assignment" 


# ATTENTION : La on connait le nombre de valeur MAIS -1 va directement chercher la dernière valeur
#print(f"La premiere note du tuple est {note[0]} et la derniere note du tuple est {note[3]}")

print(f"La premiere note du tuple est {note[0]} et la derniere note du tuple est {note[-1]}")
print("\n")

if 10 in note:
    print("10 est présent dans la liste")
else:
    print("10 n'est pas présent dans la liste")

print("\n")

print("Autre façon de faire : ")
print(10 in note)
    
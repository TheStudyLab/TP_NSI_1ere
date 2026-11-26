n = int(input("Entrez un nombre : "))

print("---- Tableau en compréhension ----\n")

t = [[0 for j in range(n)] for i in range(n)]
print(t)

print("\n")
print("---- Tableau avec append ----\n")

ta = []
for i in range (n):     # i lignes
    ta.append([])       # ligne déclarée à une liste
    for j in range(n):   
        ta[i].append(0) # ieme ligne complétée de j "0"
print(ta)

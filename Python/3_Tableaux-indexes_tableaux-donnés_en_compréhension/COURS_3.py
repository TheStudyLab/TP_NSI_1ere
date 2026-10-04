print("-------------LISTES DE LISTES------------")

L = [ [0,1,2],
      [3,4,5],
      [6,7,8] ]
print(L)

print("\n-----------------------")

print("===Parcours par indices===")

m = [ [1,3,4], [5,6,8], [2,1,3], [7,8,15] ]

for i in range(len(m)):
    for j in range(len(m[i])):
        print(m[i][j], end=" ")

    print("")

print("\n-----------------------")

print("===Parcours par éléments===")

for i in m:
    for j in i:
        print(j, end=" ")
    print("")
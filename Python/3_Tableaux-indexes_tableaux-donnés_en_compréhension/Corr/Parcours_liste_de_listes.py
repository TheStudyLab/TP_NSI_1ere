
m = [[1, "r", 4],
         [5, 6, 8],
         ["z", 1, 3],
         [7, "t", 9]]
print("m : ",m)
print("----Parcours par élément de liste de listes------")
for i in m:
    print (" i : ",i)
    for j in i:
        print("   j : ",j)
print("")

print("----Parcours par indice de liste de listes------")
for k in range(len(m)) :
    print (" k : ",k)
    for i in range(len(m[k])):
        print("  m[k][i] :",m[k][i],"   k :",k,"   i :",i,"   ")


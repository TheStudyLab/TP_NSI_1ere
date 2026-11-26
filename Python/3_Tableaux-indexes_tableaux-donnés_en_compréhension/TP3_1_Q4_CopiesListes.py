L = ['lundi', 'mardi', 'mercredi', 'jeudi']
print("L : ", L)

LCopiee = L 
LCopiee[2] = "pas école"
print("L : ", L, "LCopiee : ", LCopiee)

print("\n--------------------------")

LCop = L[:]
LCop[2] = "PAS Classe"
print("L : ", L, "LCop : ", LCop)

print("\n--------------------------")

L[2] = 99
print(L) # ['lundi', 'mardi', 99, 'jeudi']
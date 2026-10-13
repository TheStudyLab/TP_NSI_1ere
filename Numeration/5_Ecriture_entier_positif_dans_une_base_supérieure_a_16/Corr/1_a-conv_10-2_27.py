# conversion de la base 10 en base 2 - 1_a-conv10-2.py
#nombre=int(input("Nombre en base 10 à convertir en base 2 = "))
n=26
L=[]        # L contient les restes des divisions euclidiennes par 2
print("n :",n,"   ",L)
while n >= 1 :         #n//2!=0 and n//2!=1:"
    L.append(n%2)
    n=n//2
    print(" n=n//2 :",n,"   ",L)
print ("L = ",L)

print ("-----------------------------")
print ("L = ",L,"par puissance croissante")
for i in range (len(L)-1,-1,-1):
    print(L[i],end=" ")

print ("\n!!!!!-----------------------------")

resul = ""                         # chaîne qui va contenir le résultat

for j in range(len(L)):
    resul = str(L[j]) + resul      # on concatène les 0/1
    if (j + 1) % 4 == 0:
        resul = " " + resul

print("26 en base 10 =", resul, "en base 2")

print("---- Complément à un octet ----------------------------------------------")
# Compléter L à 8 bits
while len(L) < 8:
    L.insert(0, 0)                 # ajouter les 0 au début
print("*L =", L)

r = ""
for j in range(len(L)):
    r = str(L[j]) + r
    if (j + 1) % 4 == 0:
        r = "  " + r

print("*26 en base 10 =", r, "en base 2")


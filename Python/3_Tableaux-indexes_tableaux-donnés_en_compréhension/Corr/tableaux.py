##n=int(input("n:"))
##
##l= [[0 for j in range(n)] for i in range(n)]
##for j in range(n):
##    for i in range(n):
##        l[i][j] = 0
##
##l
##
##print(l)

n = int(input("n : "))

tableau_n = [[0 for j in range(n)] for i in range(n)]

tableau_n[0][0] = 1

for ligne in tableau_n:
    print(ligne)

print("\n-----------------------------------") #ou

ta=[]
for i in range (n):           # i lignes
    ta.append([])          # ligne initialisée à un liste
    for j in range(n):        # j colonnes
        ta[i].append(0)       # ieme ligne complétée de j
print(ta)

print("\n-----------------------------------")

l=[1,2,7,12,14,21,34,72]

l3=[]
for i in range(len(l)):
    if l[i]%3==0:
        l3.append(l[i])

##l3=[l[i] for i in range(len(l)) if l[i]%3==0]

l33=[]
for j in l:
    if l[i]%3==0:
        l33.append(l[i])

##l33=[j for j in l if j%3==0]

l333=[j for j in l if j%3==0]

print(l3,l33,l333)









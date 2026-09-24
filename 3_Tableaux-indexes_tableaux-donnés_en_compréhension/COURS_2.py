print("-------------LISTES PAR COMPREHENSION------------")

L = [0,1,2,3,4,5]
lcarre = []
for i in L:
    lcarre.append(i**2)
print("lcarre : ", lcarre)

print("\n-------------")

lcarre2 = [i**2 for i in L]
print("lcarre2 : ", lcarre2)

print("\n-------------")

LL =[n*n for n in L if n%2==0]
print("LL =[n*n for n in L if n%2==0] : ", LL)

print("\n-------------")


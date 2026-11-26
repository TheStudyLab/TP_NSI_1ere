#
L=[1, 2, 7, 12, 14, 21, 34, 72]
L3=[]
for i in range(len(L)):
    if L[i] % 3 == 0:
        L3.append(L[i])
for i in range(len(L3)):
    print(L3[i])
print("-------------------------------")
L33=[]
for e in L:
    if e % 3 == 0 :
        L33.append(e)
for e in L33:
    print(e)

print("-------------------------------")
L333 = [e for e in L if e % 3 == 0]
print (L333)



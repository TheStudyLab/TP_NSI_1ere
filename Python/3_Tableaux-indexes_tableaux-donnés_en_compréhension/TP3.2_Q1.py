L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

L1 = [n%2 for n in L]
print("L1 = [n%2 for n in L] : ", L1)
L2 = [n for n in L if n>4]
print("L2 = [n for n in L if n>4] : ", L2)
L3 = [n**2 for n in L if n<4]
print("L3 = [n**2 for n in L if n<4] : ", L3)
L4 = [n*4 for n in L if n%2==0]
print("L4 = [n*4 for n in L if n%2==0] : ", L4)
L5 = [n if n%2==0 else n**2 for n in L]
print("L5 = [n if n%2==0 else n**2 for n in L] : ", L5)
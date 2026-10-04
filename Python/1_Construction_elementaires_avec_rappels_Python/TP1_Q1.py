a=5
print(a)
print("a = ",a)
print("type de a : ", type(a))

b=7.5
print(b)
print("b = ",b)
print("type de b : ", type(b))

c=6,80,5
print(c)
print("c = ",c)
print("type de c : ", type(c))

t="ABCDEF"
print(t)
print("t = ",t)
print("type de t : ", type(t))

t2="abcdef"
print("t + t2 : ",t + t2,"  a+b : ",a+b)

t3=t2*3
print("t3 : ",t3)

for lettre in t:
    print(lettre)


chaine1 = "abc"
chaine2 = chaine1 + 'def'
print("chaine2 : ",chaine2,type(chaine2))
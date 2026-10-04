print("-------------LISTES PAR COMPREHENSION------------")

l = [i**3 for i in range(10,21)] # en comprehension.
print("l = [i**3 for i in range(10,21)] : ", l)

print("\n-------------LISTES IMPERATIVES------------")

li = []
for j in range(10,21):
    li.append(j**3)
print("li : ", li)
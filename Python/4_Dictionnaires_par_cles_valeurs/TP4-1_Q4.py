# dic = {0: 0,
#       1: 2,
#       2: 4,
#       3: 6}

dic = {}

for i in range(4):
    dic[i] = 2*i

print("dic = " + str(dic))

dic_modif = {}

for k in dic.keys():
    number = str(k)
    dic_modif["n°" + number] = dic[k]

print("dic_modif = " + str(dic_modif))

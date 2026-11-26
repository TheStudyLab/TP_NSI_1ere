L = [3,4.5,"a",("z",6),[],[4,"d"],{"chien":4,"chat":5}]

L.insert(2, "fleur")
print("L (L.insert(2, 'fleur')) : ", L)

L.append("choux")
print("L (L.append('choux')) : ", L)
L[6].append("pomme")
print("L (L[6].append('pomme')) : ", L)
L[5].append(("P",5))  
print("L[5] (L[5].append(('P',5))) : ", L)

L[7]["rose"]="Fleur"
print("L[7] (L[7]['rose']='Fleur') : ", L)

L.pop()
print("L (L.pop()) : ", L)
L.pop(3)
print("L (L.pop(3)) : ", L)

L.remove(4.5)
print("L (L.remove(4.5)) : ", L)

L.reverse()
print("L (L.reverse()) : ", L)

#print("--------------------------")

#L[3].append(('P',5))
#print("L[3] (L[3].append(('P',5))) : ", L)
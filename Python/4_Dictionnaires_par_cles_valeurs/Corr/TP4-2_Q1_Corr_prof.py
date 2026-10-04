#F2_exo_DIC0
l = [ 1, 1, 2, 3, 2, 1]

d={}

for i in range(len(l)):
    #ajout de l'indice à la liste dont la clé est l'élément
    if l[i] in d:
        d[l[i]].append(i)
    #création de la liste avec pour premier élément l'indice de l[i]
    else:
        d[l[i]]=[i]

print (d)

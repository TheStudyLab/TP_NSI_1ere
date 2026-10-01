l = [1,1,2,3,2,1]
# print(l)

d = {}
for i in range(len(l)):
    if l[i] in d:
        d[l[i]].append(i)
    else:
        d[l[i]] = [i]
print(d)
    
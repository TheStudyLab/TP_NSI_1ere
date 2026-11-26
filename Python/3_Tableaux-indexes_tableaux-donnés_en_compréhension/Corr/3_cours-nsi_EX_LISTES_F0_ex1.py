n = 3
t=[]
for i in range(n):
    t.append([])
    for j in range(n):
        t[i].append(0)
print(t)
t[1][2]=42
print(t)
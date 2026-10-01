# En compréhension:

print([f'{i} est pair' if i % 2 == 0 else f'{i} est impair' for i in range(0, 5)])

# En utilisant une boucle for :

l = []

for i in range(0, 5):
    if i % 2 == 0:
        l.append(f'{i} est pair')
    else:
        l.append(f'{i} est impair')

print(l)

# En utilisant une boucle while :

i = 0
li = []
while i < 5:
    if i % 2 == 0:
        li.append(f'{i} est pair')
    else:
        li.append(f'{i} est impair')
    i += 1

print(li)






def fct_2(i,j):
    print(i,j)
    i = 33
    print("La fonction fct_2 affiche : i = ", i, "j = ", j)
    
i = 1
j = 2
fct_2(16, 87)
print("i et j après fct_2 : i = ", i, "j = ", j)

print(10*"-")

def fct_3():
    global i
    i = 947
    j = 5
    print("La fonction fct_3 : i = ", i, "j = ", j)
i = 1
j = 2
fct_3()
print("i et j après fct_3 : i = ", i, "j = ", j)

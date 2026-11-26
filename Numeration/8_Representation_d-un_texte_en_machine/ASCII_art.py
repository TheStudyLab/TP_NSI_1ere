print("1. La méthode parfaite :)")

l1 = "xxxxxxxxxxxxxxxxxxxx"
l2 = "xxx//////////////xxx"
l3 = "xxx##############xxx"

print(f"\n {l1} \n {l1} \n {l1} \n {l2} \n {l2} \n {l3} \n {l2} \n {l2} \n {l1} \n {l1} \n {l1} \n ")

print("2. La méthode de cours (avec for) \n")

for i in range(11):
    if (i >= 0 and i <= 2) or (i >= 8 and i <= 10):
        print("x"*20)
    if (i >= 3 and i <= 4) or (i >= 6 and i <= 7):
        print("x"*3 + "/"*14 + "x"*3)
    if i == 5 :
        print("xxx##############xxx")

print("\n 3. La méthode de cours (en comprehension) \n")

for l in range(11): 
    print("x"*20 if l<=2 or l>=8 else "x"*3 + ("#" if l==5 else "/")*14 + "x"*3)


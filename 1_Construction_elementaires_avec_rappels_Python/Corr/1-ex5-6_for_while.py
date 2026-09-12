# exercice 5

print ("Boucle 'for' :  ")
for i in range(0,102,2):
    print(i,end=" ")


print ("\nBoucle 'while' :  ")
i=0
while i<=100:
    print (i,end=" ")
    i=i+2

print("\n-----------------------------\n")

#exercice 6
#a=input("Appuyez sur une touche")
for i in range(1,2):
    print ("Table de multiplication par ",i)
    for j in range(1,11):
        print (j," fois ",i," = ",j*i)

print("\n")

for i in range(1,2):
    print (f"Table de multiplication par {i}")
    for j in range(1,11):
        print (f"{j} fois {i} = {j*i}")


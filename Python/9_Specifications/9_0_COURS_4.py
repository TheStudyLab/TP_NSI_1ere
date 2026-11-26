# 1.

def fct(x=1):
    return x

print(fct())

# 2.

def se_presenter(prenom, nom="Marin"):
    return(prenom, nom)

d,e = se_presenter("Jean")
print("Bonjour",d,". Mon nom est ",e,"!")
f,g = se_presenter("Jean", "Brassart")
print("Bonjour",f,". Mon nom est ",g,"!")
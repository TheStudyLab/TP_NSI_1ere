def se_presenter(prenom, nom="Martin"):
    return(prenom,nom)

a,b = se_presenter("Jean")
print("Bonjour", a, ". Mon nom est", b, "!")
c,d = se_presenter("Jean", "Brassart")
print("Bonjout", c, ". Mon nom est", d, "!")

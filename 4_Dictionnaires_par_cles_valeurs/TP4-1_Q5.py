t = {"janvier": -5,
    "février": 2,
    "Novembre": 12,
    "Décembre": 7
    }

temp = 0
maximum = []

for cle, valeur in t.items():
    if int(valeur) > temp:
        temp = valeur
        maximum = [cle, valeur]

print(maximum)
print("[\'Novembre\', 12]")
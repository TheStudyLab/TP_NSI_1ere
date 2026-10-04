temp = {'Janvier': -5, 
        'Février': 2, 
        'Décembre': 7, 
        'Novembre': 12,}

ma = -110
for cle , valeur in temp.items():
    if valeur > ma:
        ma = valeur
        mois = cle

print(f"('{mois}', {ma}).")

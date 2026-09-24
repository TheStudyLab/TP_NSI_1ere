"""
À vous de prendre la vie dans le bon sens
Poème à lire dans les 2 sens pour redonner confiance.
Comment changer le sens de ce poème ?
"""
poeme = (
['Je', 'suis', 'un', 'gros', 'nul'],
['Personne', 'n’ose', 'penser', 'que'],
['Je', 'suis', 'un', 'gros', 'nul'],
['Personne', 'n’ose', 'penser', 'que'],
['Je', 'suis', 'capable', 'd’accomplir', 'de', 'grandes', 'choses'],
['Je', 'sais', 'que'],
['Je', 'raterai', 'tout', 'ce', 'que', "j'entreprendrai"],
['Je', 'ne', 'crois', 'plus', 'que'],
['Je', 'peux', 'réussir'],
['Je', 'suis', 'persuadé', 'que'],
['Je', 'ne', 'vaux', 'rien'],
['J’ai', 'arrêté', 'de', 'me', 'dire', 'que'],
['J’ai', 'confiance', 'en', 'moi'],
['Je', 'suis', 'convaincu', "d'une", 'chose', ':'],
['Je', 'suis', "quelqu'un", "d'inutile"],
['Et', 'ce', 'serait', 'idiot', 'de', 'penser', 'que'],
['Je', 'suis', 'une', 'belle', 'personne'])

for i in range(len(poeme)-1,0,-1):      
    
    for j in range(len(poeme[i])):      
        print(poeme[i][j], end=' ')     
    print (" ")      







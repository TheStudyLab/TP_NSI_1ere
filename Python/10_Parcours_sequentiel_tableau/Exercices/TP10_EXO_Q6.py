def nb_repetitions(elt, tab):
    assert type(tab) == list, "The parameter 'tab' must be a list"
    
    cpt = 0

    for i in range(len(tab)):

        if tab[i] == elt:
            cpt += 1
            
    return cpt

print(nb_repetitions(5, [2, 5, 3, 5, 6, 9, 5]))
print(nb_repetitions("A", ["A", "D", "A", "L", "O", "V", "L", "A", "C", "E"]))

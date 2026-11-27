def recherche_indices_classement(elt, tab):
    assert type(elt) == int, "The parameter 'elt' must be an integer"
    assert type(tab) == list, "The parameter 'tab' must be a list"
    
    tab_under_elt = []
    tab_equal_elt = []
    tab_upper_elt = []
    
    for i in range(len(tab)):
        assert type(tab[i]) == int, "The list must contains integer"

        if tab[i] < elt:
            tab_under_elt.append(i)
        elif tab[i] == elt:
            tab_equal_elt.append(i)
        elif tab[i] > elt:
            tab_upper_elt.append(i)
    
    return tab_under_elt, tab_equal_elt, tab_upper_elt

print(recherche_indices_classement(3, [1, 3, 4, 2, 4, 6, 3, 0]))

def indice_maxi(tab):
    assert tab, "You must give a plain list"
    assert type(tab) == list, "The parameter must be a list"        
    
    max_tab = tab[0]
    max_tab_indices = []
    
    for i in range(len(tab)):
        assert type(tab[i]) == int, "The list must contains integer"
        
        if tab[i] > max_tab:
            max_tab = tab[i]
            max_tab_indices = [i]
        elif tab[i] == max_tab:
            max_tab_indices.append(i)
    
    return max_tab, max_tab_indices

print(indice_maxi([5, 3, 5, 7, 5, 7, 6]))

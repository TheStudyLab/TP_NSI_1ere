def min_max(tab):
    if not tab:
        return {"min": None, "max": None}

    min_tab = tab[0]
    max_tab = tab[0]

    for val in tab[1:]:
        if val < min_tab:
            min_tab = val
        if val > max_tab:
            max_tab = val

    return {"min": min_tab, "max": max_tab}


print(min_max([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]))

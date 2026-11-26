l = [4, 48, 3, 9, 4, 48, 7, 4, 3]

def min_max_for(l):
    if len(l) == 0:
        return None, None

    mini = l[0]
    maxi = l[0]
    for number in l:
        if number > maxi:
            maxi = number
        if number < mini:
            mini = number
    return mini, maxi

print("Minimum et maximum de la liste l (methode for) : ", min_max_for(l))

def min_max_while(l):
    if len(l) == 0:
        return None, None

    mini = l[0]
    maxi = l[0]
    i = 0
    while i < len(l):
        if l[i] > maxi:
            maxi = l[i]
        if l[i] < mini:
            mini = l[i]
        i += 1
    return mini, maxi

print("Minimum et maximum de la liste l (methode while) : ", min_max_while(l))
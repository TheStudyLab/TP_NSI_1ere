liste = [4, 7, 3, 12, 5, 17, 1, 19]

def minimum(l):
    min_val = l[0]
    
    for element in l:
        if element < min_val :
            min_val = element
    
    return min_val

print( f"minimum : {minimum(liste)} vs min: {min(liste)}")

def maximum(l):
    max_val = l[0]
    
    for element in l:
        if element > max_val :
            max_val = element
    
    return max_val

print( f"maximum : {maximum(liste)} vs max: {max(liste)}")

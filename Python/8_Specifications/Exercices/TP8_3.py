def Pythagore(a, b, c):
    if a > b and a > c:
        return(a**2 == b**2 + c**2)
    elif b > a and b > c:
        return(b**2 == a**2 + c**2)
    elif c > a and c > b:
        return(c**2 == a**2 + b**2)

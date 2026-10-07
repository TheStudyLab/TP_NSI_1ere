# print(hex(int(input("Enter a number : "))))

def hexadecimal(n):
    if n == 0:
        return "0x0"
    
    # Caractères hexadécimaux disponibles
    symboles = "0123456789ABCDEF"
    resultat = ""
    
    valeur = n
    while valeur > 0:
        reste = valeur % 16
        resultat = symboles[reste] + resultat
        valeur //= 16
        
    return "0x" + resultat

user_field  = int(input("Entrez un nombre entier... "))

m2 = user_field % 2
m3 = user_field % 3

if ( m2 == 0 ) :
    print("Ce nombre est pair")
    if ( m3 == 0) :
        print("Ce nombre est un multiple de 3")
else :
    if ( m3 == 0) :
        print("Ce nombre est impair")
        print("Ce nombre est un multiple de 3")
    else:
        print("Ce nombre n'est ni pair ni un multiple de 3")
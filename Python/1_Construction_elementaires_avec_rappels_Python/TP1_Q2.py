a = 3
b = 3
if ( a > 5 or b != 3) :
    b = 4
else :
    b = 2
print(b)
# résultat attendu : 2

a = 7
b = 12
if ( a < 5) :
    b = b - 4
if ( b >= 10) :
    b = b + 1
print(b)
# résultat attendu : 13

a = 2
b = 0
if ( a < 0 ) :
    b = 1
elif ( a > 0 and a < 5 ) :
    b = 2
else :
    b = 3
print(b)
#résultat attendu : 2
def min_max(t):
    mi = t[0]
    ma = t[0]

    for i in range(len(t)):
        if t[i] > ma:
            ma = t[i]
        if t[i] < mi:
            mi = t[i]

    return (mi, ma)

print(f"Le minimum et le maximum du tuple sont : {min_max((5, 2, 8, 4, 9))}")
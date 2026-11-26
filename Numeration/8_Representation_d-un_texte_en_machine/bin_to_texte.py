binaire = ["01000010", "01110010", "01100001", "01110110", "01101111", "00100001"]

mot = ""
for b in binaire:
    vd = int(b, 2)
    car = chr(vd)
    mot = mot + car

print(mot)  # Affiche : Bravo!
nimet = set()
uusinimi = 1
while uusinimi != "":
    uusinimi = input("antaisitko nimen?:")
    if uusinimi in nimet:
        print("Aiemmin syötetty nimi")
    elif uusinimi != "":
        nimet.add(uusinimi)
        print("Uusi nimi")
    else:
        print("Ohjelma loppui.")

print("lopulliset nimet:")
for nimi in nimet:
    print(nimi)
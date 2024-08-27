numerot = []
x = 0
while x != "":
    x = input("anna luku tai lopeta jättämällä tämä tyhjäksi\n:")
    numerot.append(x)
numerot.sort()
print("pienin numero", numerot[1])
print("suurin numero", numerot[-1])
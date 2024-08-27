pituus = int(input("kuinka monta senttimetriä pitkä kuha on?\n:"))
if pituus < 37 and pituus != 36:
    print("heitä takaisin veteen")
    print(f"tarvitset vielä: {37-pituus} senttimetriä")
elif pituus == 36 :
    print("heitä takaisin veteen, tarvitset vielä yhden senttimetrin.")
else :
    print("saa syödä!")
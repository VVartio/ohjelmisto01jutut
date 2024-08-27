import random
noppa = random.randint(1,10)
arvaus = int(input("arvaa numero 1-10\n:"))
while arvaus != noppa:
    if arvaus < noppa:
        print("liian pieni arvaus")
        arvaus = int(input("yritä uudelleen\n:"))
    else:
        print("liian suuri arvaus")
        arvaus = int(input("yritä uudelleen\n:"))
print("oikein!")
kauttaja = input("käyttäjä\n:")
salasana = input("salasana\n:")
counter = 1
while kauttaja != "python" or salasana != "rules":
    if counter == 5:
        print("pääsy evätty")
        break
    print("yritä uudelleen")
    kauttaja = input("käyttäjä\n:")
    salasana = input("salasana\n:")
    counter += 1
else:
    print("tervetuloa")
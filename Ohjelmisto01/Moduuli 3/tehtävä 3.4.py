vuosi = int(input("Anna vuosiluku\n:"))
if vuosi%100 == 0 and vuosi%400 == 0:
    print("vuosi on karkausvuosi")
elif vuosi%4 == 0 and vuosi%100 != 0:
    print("vuosi on karkausvuosi")
else:
    print("vuosi ei ole karkausvuosi")
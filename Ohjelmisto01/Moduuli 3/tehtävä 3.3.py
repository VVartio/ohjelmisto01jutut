sukupuoli = input("Syötä biologinen sukupuolesi\n:")
arvo = int(input("Entä hemglobiini arvosi? (g/l)\n:"))
if sukupuoli == "mies" or sukupuoli == "Mies":
    if arvo >= 134 and arvo <= 195:
        print("hemoglobiiniarvo on normaali (:")
    elif arvo < 134:
        print("hemoglobiiniarvosi on alhainen")
    else:
        print("hemoglobiiniarvosi on korkea")
if sukupuoli == "nainen" or sukupuoli == "Nainen":
    if arvo >= 117 and arvo <= 175:
        print("hemoglobiiniarvosi on normaali")
    elif arvo < 117:
        print("hemoglobiiniarvosi on alhainen")
    else:
        print("hemoglobiiniarvosi on korkea")
tuuma = 0
while tuuma >= 0:
    tuuma = float(input("Tuumien määrä?\n:"))
    cm = tuuma * 2.54
    if tuuma >= 0:
        print(cm)
    if tuuma < 0:
        print("ohjelma loppui")
        break

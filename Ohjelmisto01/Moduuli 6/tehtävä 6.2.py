import random
dicemax = int(input("kuinka monta tahkoa?:"))
def dice():
    dicenum = random.randint(1,dicemax)
    while dicenum != dicemax:
        dicenum = random.randint(1,dicemax)
        print(dicenum)
    else:
        return
dice()
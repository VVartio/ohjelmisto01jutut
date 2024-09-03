import random
def dice():
    dicenum = random.randint(1,6)
    while dicenum != 6:
        dicenum = random.randint(1,6)
        print(dicenum)
    else:
        return
dice()
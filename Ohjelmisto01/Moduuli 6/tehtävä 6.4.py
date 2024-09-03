import random
list = []

def listcalc(list):
    amount = 0
    for i in list:
        amount += i
    print(amount)
    return

def randomiser():
    i = random.randint(0,100)
    global list
    for i in range(i):
        list.append(random.randint(0,100))
    return

randomiser()
listcalc(list)
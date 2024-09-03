import random
list = []
def randomiser():
    global list
    i = random.randint(0,100)
    for i in range(i):
        list.append(random.randint(0,100))
    return
def main(list):
    only_even = []
    for i in list:
        if i % 2 == 0:
            only_even.append(i)
    print(f"secondary list: {only_even}")
    print(f"main list:{list}")
    return
randomiser()
main(list)
import math
def costeffectiveness():
    price = int(input("what did the pizza cost?:"))
    size = int(input("How big was the diameter of the pizza?:"))
    truesize = math.pi * size ** 2
    cost1 = truesize / price * 0.0001
    price = int(input("what did the second pizza cost?:"))
    size = int(input("How big was the diameter of the second pizza?:"))
    truesize = math.pi * size ** 2
    cost2 = truesize / price * 0.0001
    print("first pizza cost effectiveness:", cost1)
    print("second pizza cost effectiveness:", cost2)
    if cost1 > cost2:
        print("pizza 1 is more effective")
    else:
        print("pizza 2 is more effective")
    return

costeffectiveness()
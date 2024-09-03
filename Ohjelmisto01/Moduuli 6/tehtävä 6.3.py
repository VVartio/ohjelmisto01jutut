def oilconverter():
    amount = int(input("How much oil do you have? In gallons of course, we aren't savages:"))
    while amount >= 0:
        litres = amount * 3.785
        print(f"Gotcha! That's actually {litres} litres. Get educated!")
        amount = int(input("Do you want to try again with the superior gallons?:"))
    return
oilconverter()
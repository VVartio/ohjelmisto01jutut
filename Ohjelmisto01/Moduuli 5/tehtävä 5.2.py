list = []
listadder = 0
while listadder != "":
    listadder = input("anna numero tai lopeta panamalla ENTER\n:")
    if listadder == "":
        break
    list.append(listadder)
list.sort(reverse=True)
print(list[0:4])
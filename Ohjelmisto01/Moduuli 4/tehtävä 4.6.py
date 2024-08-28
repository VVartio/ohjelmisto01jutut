import random

maara = int(input("määrä\n:"))
n = 0
counter = 0
while maara != counter:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    counter += 1
    if x**2+y**2 < 1:
        n += 1
pi = 4*n/maara
print(pi)
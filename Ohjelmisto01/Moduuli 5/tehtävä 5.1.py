import random
dice = int(input("kuinka monta noppaa?\n:"))
sum = 0
for i in range(1, dice + 1):
    sum += random.randint(1,6)
print(f"noppien silmälukujen summa: {sum}")
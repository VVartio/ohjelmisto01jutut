num = int(input("Enter a number: "))

if num > 1 :
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "IsNotAPrime")
            break
    else:
        print(num, "IsPrime")

else:
    print("IsNotAPrime")
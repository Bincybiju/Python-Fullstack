n=int(input("enter the number"))
if n%2==0:
    if n%5==0:
        print(n, " is divisible by 2 and 5")
    else:
        print(n," is not divisible by 2 and 5")
else:
    print(n," is not divisible by 2 and 5")
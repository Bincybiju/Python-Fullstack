num = int(input("Enter a number : "))  
i = 2
while i < num:
    if num % i == 0:
        print("The entered number is not a prime number")
        break
    i=i+1
else:
    print("The entered number is a prime number")
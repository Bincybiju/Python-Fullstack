num=int(input("Enter the number : "))
if num%5==0 and num%6==0:
    print("Is this number divisible by 5 and 6? True")
else:
    print("Is this number divisible by 5 and 6? False")
if num%5==0 or num%6==0:
    print("Is this number divisible by 5 or 6? True")
    if num%5==0 and num%6==0 :
        print("Is this number divisible by 5 or 6,but not both? false")
    else:
        print("Is this number divisible by 5 or 6,but not both? True")
else:
    print("Is this number divisible by 5 or 6? False")
    
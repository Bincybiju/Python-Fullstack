num=int(input("Enter the number : " ))
temp=num
rev=0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
print("Reverse of number is ",rev)
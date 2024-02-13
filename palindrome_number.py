# num=int(input("Enter the number : " ))
# temp=num
# rev=0
# while num>0:
#     rem=num%10
#     rev=rev*10+rem
#     num=num//10
# if rev==temp:
#     print("palindrome number")
# else:
#     print("Not palindrome number")

for i in range(1,1000):
    n=str(i)
    if n==n[::-1]:
        print(i)

# i = 1
# while i < 10 :
#     print(i) 
#     i +=1
# else: # Works when codnition becomes wrong 
#     print("The value exeeds 10")
# i = 0 
# while i < 11: # False
#     print(i)
#     # if i == 5:
#     #     break
#     i = i + 1 
# else :
#     print("The code is broken")

num = int(input("Enter a number : ")) # 213
temp = num
rev = 0

while num > 0:
    rem = num % 10
    rev = rev * 10 + rem # 3
    num = num // 10  # num = 0
print("The reverse of the number is : ", rev)
if rev == temp:
    print("It is a palindrom : ", temp)
else:
    print("Not Palindrome")






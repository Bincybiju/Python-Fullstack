n=input("enter a string : ")

r=" "
for i in range(len(n)-1,-1,-1):
    r=r+n[i]
print(r)


# for i in n:
#     temp=n[::-1]
# print("Reverse of string is : ",temp)
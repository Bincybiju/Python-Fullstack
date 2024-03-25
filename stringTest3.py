str1=input("Enter first string : ")
str2=input("Enter second string : ")
first=str1[0]+str2[0]
mid = str1[len(str1) // 2] + str2[len(str2) // 2]
last=str1[-1]+str2[-1]
print(first+mid+last)
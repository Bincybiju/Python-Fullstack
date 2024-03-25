str=input("Enter a string : ")
first=str[:2]
last=str[-2:]
length=len(str)
if length<2:
     print("Empty string")
else:
     print(first+last)

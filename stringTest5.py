str=input("Enter a string : ")
upper=0
lower=0
digits=0
symbols=0
for i in range(len(str)):
    if str[i].isupper():
        upper=upper+1
    elif str[i].islower():
        lower=lower+1
    elif str[i].isdigit():
        digits=digits+1
    else:
        symbols=symbols+1
print("Number of upper case : ",upper)
print("Number of lower case : ",lower)
print("Number of digits: ",digits)
print("Number of special symbols: ",symbols)
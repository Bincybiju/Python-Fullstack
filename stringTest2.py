str=input("Enter a string : ")
if len(str)>3:
    if str.endswith("ing"):
        print(str+"ly")
else:
    print(str+"ing")

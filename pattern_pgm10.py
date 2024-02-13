row=int(input("Enter number of rows : "))
if row%2!=0:
    for i in range(1,row//2+1):
        for j in range(i):
            print("*",end=" ")
        print()
    for i in range(row//2+1,0,-1):
        for j in range(i):
            print("*",end=" ")
        print()
else:
    print("pattern will not be proper")

# *
# * *
# * * *
# * *
# *


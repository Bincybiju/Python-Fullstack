row=int(input("Enter number of rows : "))
for i in range(row,0,-1):
    for j in range(i):
        if i==row or i==1:
                print("*",end=" ")
        elif j==0 or j==i-1:
                print("*",end=" ")
        else:
                print(" ",end=" ")             
    print()

# * * * * *
# *     *
# *   *
# * *
# *
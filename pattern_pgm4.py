# * * * *
#   * * *
#     * *
#       *

row=int(input("enter the number of rows"))
for i in range(0,row):
    for j in range(i):
        print(" ",end=" ")
    for k in range(row-i,0,-1):
        print("*",end=" ")
    print()
        
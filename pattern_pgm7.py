row=int(input("Enter number of rows : "))
for i in range(row,0,-1):
    for j in range(0,row-i):
        print(" ", end=" ")
    for k in range((2*i)-1):
        print("*", end=" ")
    print("")

# * * * * *
#   * * *
#     *
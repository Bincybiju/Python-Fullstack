row=int(input("Enter number of rows : "))
if row%2!=0:
    for i in range(row//2,-1,-1):
        for j in range(0,row//2-i):
            print(" ", end=" ")
        for k in range((2*i)+1):
            print("*", end=" ")
        print("")
    for i in range(1,row//2+1):
        for j in range(0,row//2-i):
            print(" ", end=" ")
        for k in range((2*i)+1):
            print("*", end=" ")
        print("")
else:
    print("pattern will not be proper")

# * * * * *
#   * * *
#     *
#   * * *
# * * * * *
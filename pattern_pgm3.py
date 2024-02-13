#       *
#     * *
#   * * *
# * * * *
rows= int(input("enter number of rows : "))
for i in range(rows,0,-1):
    for j in range(0,rows-i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print("")
# n= int(input("enter number of rows : "))
# for i in range(1,n+1):
#      print(" "*(n-i)+"*"*i)

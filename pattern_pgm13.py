rows= int(input("enter number of rows : "))
for i in range(0,rows):
    for j in range(1,rows-i):
        print(" ", end=" ")
    for k in range((2*i)+1):
        if i==rows-1 or i==0:
            print("*",end=" ")
        elif k==0 or k==2*i:
            print("*",end=" ")       
        else:
            print(" ",end=" ")
    print("")
    
#         *
#       *   *
#     *       *
#   *           *
# * * * * * * * * *
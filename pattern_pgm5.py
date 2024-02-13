rows= int(input("enter number of rows : "))
for i in range(0,rows):
    for j in range(1,rows-i):
        print(" ", end=" ")
    for k in range((2*i)+1):
        print("*", end=" ")
    print("")
    
#           *
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *
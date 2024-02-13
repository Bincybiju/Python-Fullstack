rows= int(input("enter number of rows : "))
for i in range(0,rows):
    for j in range(0,rows-i):
        print(" ", end=" ")
    for k in range((2*i)+1):
        print("*", end=" ")
    print("")
for i in range(rows,-1,-1):
    for j in range(0,rows-i):
        print(" ", end=" ")
    for k in range((2*i)+1):
        print("*", end=" ")
    print("")

#           *
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *
# * * * * * * * * * * *
#   * * * * * * * * *
#     * * * * * * *
#       * * * * *
#         * * *
#           *


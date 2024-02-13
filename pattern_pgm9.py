r=int(input("Enter number of rows : "))
if r%2!=0:
    for i in range(r):
        if i<=r//2:
            for j in range(r//2-i):
                print(" ",end=" ")
            for k in range(2*i+1):
                 print("*",end=" ")
        else:
            for j in range(i-r//2):
                print(" ",end=" ")
            for k in range(2*(r-i)-1):
                 print("*",end=" ")
        print()
        
#     *
#   * * *
# * * * * *
#   * * *
#     *
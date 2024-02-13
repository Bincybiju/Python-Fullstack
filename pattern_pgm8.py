rows= int(input("enter number of rows : "))
num=1
for i in range(0,rows):
    num=1
    for j in range(0,i+1):
        print(num,end=" ")
        num=num+1
    print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4
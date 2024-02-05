num=int(input("enter number of rows : "))
number=1
for i in range(num):
    for j in range(i+1):
        print(number,end=" ")
        number=number+1
    print()
        
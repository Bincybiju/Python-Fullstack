r=int(input("Enter number of rows : "))
c=int(input("Enter number of columns : "))
l=[]
print("Enter the matrix elements :")
for i in range(r):
    li=[]
    for j in range(c):
        num=int(input())
        li.append(num)
    l.append(li)
print(l)
for i in range(r):
    for j in range(c):
        print(l[j][i],end=" ")
    print()
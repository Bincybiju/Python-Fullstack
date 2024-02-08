l=[1,2,3,2,4,4,2,5,6,2]
num=int(input("Enter the searching element :"))
c=0
f=1
for i in l:
    if num==i:
        c=c+1
        f=0
if f==0:
    print(f"The number {num} exist {c} times")
else:
    print("The number not exist in the list")

for i in range(len(l)):
    if l[i]==num:
        print("Index position :" ,i)


        
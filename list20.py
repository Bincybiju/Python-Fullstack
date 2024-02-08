num=int(input("Enter the number of students : "))
l1=[]
l2=[]
for i in range(num):
    name=input("Enter your name :")
    mark=int(input("Enter your mark :"))
    l1.append(name)
    l2.append(mark)
avg=sum(l2)/2
print("Average score is ",avg)

print("Below average students:")
for i in range(num):
    if l2[i]<avg:
        print("Better luck next time  " ,l1[i])
    

li=l2[0]
for i in l2:
    if i>li:
        li=i
        print("Highest test score :",li)

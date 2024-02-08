l=[]
print("Enter the numbers : ")
for i in range(10):
    num=int(input())
    if num%2==0:  
        l.append(num)
print("Even numbers : ",l)
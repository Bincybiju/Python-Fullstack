l=[]
even=0
odd=0
print("Enter the numbers : ")
for i in range(10):
    num=int(input())  
    l.append(num)
print(l)
for j in l:
    if j%2==0:
       even=even+1
    else:
        odd+=1
    
print("Number of even numbers : ",even)
print("Number of odd numbers : ",odd)
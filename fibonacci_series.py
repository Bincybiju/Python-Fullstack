lim=int(input("enter a limit : "))
i=1
n1=0
n2=1
print("fibonacci series are:")
while i<=lim:
    print(n1) 
    n3=n1+n2 
    n1=n2
    n2=n3
    i=i+1


# n = int(input("Enter length of Fibonacci series: "))
# num1 = 0
# num2 = 1
# next_number = 0
# count = 1
  
# while(count <= n):
#     print(next_number, end=" ")
#     count += 1
#     num1 = num2
#     num2 = next_number
#     next_number = num1 + num2
#     t_number = num1 + num2
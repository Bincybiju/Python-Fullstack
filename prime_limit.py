num=int(input("Enter a limit : "))
for i in range(2,num):
    for j in range(2,i):
        if i%j == 0:
            break
    else: 
        print("Number is prime :", i)
    
    
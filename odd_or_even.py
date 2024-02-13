import random
sum=0
name=input("Enter your name :")
print("Hi",name,"Welcome to the Odd or even game")
while True:
    num=int(input("Hit any number from 1-6 : "))
    if num not in[1,2,3,4,5,6]:
        print("Hit the correct number")
    else:
        r=(random.randint(1,6))
        print(r)
        if num==r:
            print("You are out")
            print("Total score is:",sum)
            break
        else:
            sum=sum+num
            print("Your score is :",sum)
        
  

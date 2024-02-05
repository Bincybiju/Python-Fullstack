import random
r=(random.randint(0,9))
name=input("Enter your name :")
print("Hi",name,"Welcome to the Guess Game")
for i in range(3):
    num=int(input("Guess any number from 0-9 : "))
    if num==r:
        print("You win the game")
        break
    else:
        if i==2:
            print("You lost the game")
        else:
             print("Try again")
print("The number is ",r)
print("Game over")  

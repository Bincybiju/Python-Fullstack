print("SIMPLE CALCULATOR")
print("1. ADD")
print("2. SUB")
print("3. Multiply")
print("4. DIV")
print("5. Exit")
while True:
    choice=int(input("Enter your choice : "))
    if choice == 5:
        break
    elif choice not in [1,2,3,4]:
        print("choose the correct option")
    else:       
        num1=float(input("Enter the first number : "))
        num2=float(input("Enter the second number : "))
        if choice==1:
            print(num1+num2)
        elif choice==2:
            print(num1-num2)
        elif choice==3:
            print(num1*num2)
        elif choice==4:
            print(num1/num2)
        
    

    
    
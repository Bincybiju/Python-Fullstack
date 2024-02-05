def calculator():    
    while True:
        print("SIMPLE CALCULATOR")
        print("1. ADD")
        print("2. SUB")
        print("3. Multiply")
        print("4. DIV")
        print("5. Exit")
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
def mult():
    num=int(input("Enter a number : "))
    for i in range(1,11):
        print(i,"*",num,"=",num*i)
def notes():  
    while True:
        print("1. Create notes")
        print("2. View notes")
        print("3. Exit")
        choice=int(input("Enter your choice : "))
        if choice == 3:
            break
        elif choice not in [1,2]:
            print("choose the correct option")
        else: 
            if choice==1: 
                head=input("Type the heading of the notes... ")
                f=open(f"{head}.txt","x")
                f.close()
                con=input("Write the content in notes ")
                f=open(f"{head}.txt","w")
                f.write(con)
                f.close()
                print("Your note is created ")
            elif choice==2:
                head=input("Which note you want to view ?")
                f=open(f"{head}.txt","r")
                print(f.read())
                f.close()        
while True:  
    print("1.Calculator \n2.Multiplication table \n3.Keep notes\n4.Exit")
    choice=int(input("Enter your choice : "))
    if choice == 4:
        break
    elif choice not in [1,2,3]:
        print("choose the correct option")
    else:
        if choice==1:
            calculator()
        elif choice==2:
            mult()
        elif choice==3:
            notes()
        


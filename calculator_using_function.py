print("SIMPLE CALCULATOR")
print("1. ADD")
print("2. SUB")
print("3. Multiply")
print("4. DIV")
print("5. Exit")
def add(a,b):
    print("sum is :",a+b)
def sub(a,b):
    print("difference is :",a-b)
def mul(a,b):
    print("product is :",a*b)
def div(a,b):
    print("division is :",a/b)
while True:  
    choice=int(input("Enter your choice : "))
    if choice == 5:
        break
    elif choice not in [1,2,3,4]:
        print("choose the correct option")
    else:
        n1=int(input("Enter first number :"))
        n2=int(input("Enter second number :"))
        if choice==1:
            add(n1,n2)
        elif choice==2:
            sub(n1,n2)
        elif choice==3:
            mul(n1,n2)
        elif choice==4:
            div(n1,n2)
        
    






d={"Bincy":{"name":"Bincy","phone":[7559816650,9876543218],"gmail":"bincybiju50@gmail.com"},"soni":{"name":"soni","ph":[8546789546,9879879870],"gmail":"soni@gmail.com"}}
print("1:create")
print("2:view")
print("3:update")
print("4:delete")
print("5.exit")
while True:
    op=int(input("Enter an option : "))
    if op == 5:
        break
    elif op not in [1,2,3,4]:
        print("choose the correct option")
    else:
        if op==2:
            vi=input("Enter the name of contact you want to view :")
            if vi in d.keys():
                print(d[vi])
            else:
                print("user not found")
        elif op==4:
            dele=input("Which name you want to delete : ")
            if dele in d:
                d.pop(dele)
                print(d) 
            else:
                print("user not found") 
        elif op==3:
            con=input("Which contact you want to update : ")
            if con in d.keys():
                print("1:phone")
                print("2:gmail")
                print("3:name")
                num=int(input("Which field you want to update : "))
                if num==1:               
                    print("1:phone1")
                    print("2:phone2")
                    print("3:Both")
                    phn=int(input("Which phone number you want to update : "))
                    if phn==1:                  
                        phne1=int (input("Enter the new phone number : "))
                        d[con]["phone"][0]=phne1
                        print(d)
                    elif phn==2:
                            phne2=int(input("Enter the new phone number 2: "))
                            d[con]["phone"][1]=phne2
                            print(d)
                    elif phn==3:
                            phne1=int(input("Enter the phone number 1: "))
                            phne2=int(input("Enter the phone number 2: "))
                            d[con]["phone"][0]=phne1
                            d[con]["phone"][1]=phne2
                            print(d)
                    elif phn not in [1,2,3]:
                        print("choose the correct option")

                elif num==2:
                    gm=input("Enter the new gmail id  : ")
                    d[con]["gmail"]=gm
                    print(d)
                    
                elif num==3:
                        nn=input("Enter the new name  : ")
                        d[con]["name"]=nn 
                        d[nn]=d[con]
                        del d[con]
                        print(d) 
                else:
                    print("choose the correct option")
            else:
                        print("user not found")           
                    
            
            

        elif op==1:
            name=input("Enter the name : ")
            if name not in d.keys():
                phone1=int(input("Enter the phone number1 : "))
                phone2=int(input("Enter the phone number2 : "))
                gmail=input("Enter the gmail id : ")  
                d1={}          
                d1["name"]=name
                d1["phone"]=[phone1,phone2]  
                d1["gmail"]=gmail
                print(d1)
                d[name]=d1    
                print(d)
            else:
                print("User already found")
   




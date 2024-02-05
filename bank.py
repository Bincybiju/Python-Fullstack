d={"Bincy":"bincybiju","Aby":"aby2000"}
di={2345667778:{"ac":2345667778,"pin":3456,"name":"sona","ph":8963214444,"bal":10000},5645667778:{"ac":5645667778,"pin":4456,"name":"monu","ph":9063214444,"bal":20000}}
while True:
    print("Login as \n 1.staff \n 2.customer")
    num=int(input("Enter your choice :"))
    if num not in[1,2]:
        print("Enter correct choice")
    else:      
        if num==1:
            user=input("Enter your username :")
            pw=input("Enter your password :")
            if user in d and d[user]==pw:
                print(".....Login successful.....")   
            else:
                print("Invalid username or password.Try again...")
            while True:
                print("1.Add customer \n2.Customer deposit \n3.Exit")
                c=int(input("Enter your choice :"))
                if c not in[1,2,3]:
                    print("Enter correct choice")
                else:
                    if c==1:
                        ac=int(input("Enter Account number of customer:"))
                        name=input("Enter the name :")
                        ph=input("Enter phone number :")
                        bal=int(input("Enter the balance :"))
                        d1={}  
                        d1["ac"]=ac
                                
                        d1["name"]=name
                        d1["ph"]=ph
                        d1["bal"]=bal
                        di[ac]=d1    
                        print(di)
                        # f=open(f"{ac}.txt","x")
                        # f.close()
                        # f=open(f"{ac}.txt","w")
                        # f.write( f"{ac} \n{name} \n{ph}\n{bal}")
                        # f.close()
                    elif c==2:
                        ac=int(input("Enter your account number :"))
                        if ac in di.keys():
                            de=int(input("Enter the amount you want to deposit :"))
                            print("Net Balance :",di[ac]["bal"]+de)
                        else:
                            print("Invalid account number")
                    elif c==3:
                        break
        elif num==2:
            a=int(input("Enter your account number :"))
            if "pin" not in di[a].keys():
                pin=int(input("Enter your pin : "))
                pi=int(input("confirm pin number : "))
                if pin==pi:
                    di[ac]["pin"]=pin
                    print(di)
                else:
                    print("Enter correct pin")
            else:
                while True:
                    print("1.Balance enquiry\n2.Deposit\n3.Withdrawal\n4.update details\n5.Exit")
                    ch=int(input("Enter your choice :"))
                    if ch not in [1,2,3,4]:
                        print("choose the correct option")
                    elif ch==5:
                        break
                    else:                                
                        if ch==1:
                            if a in di.keys():
                                print("Your net balance is :",di[a]["bal"])
                            else:
                                print("Invalid account number")
                        elif ch==2:
                            if a in di.keys():
                                am=int(input("Amount that you want to deposit :"))
                                print("Your net balance :",di[a]["bal"]+am)
                            else:
                                print("Invalid account number")
                        elif ch==3:
                            if a in di.keys():
                                wi=int(input("Amount that you want to withdraw :"))
                                print("Your net balance :",di[a]["bal"]-wi)
                            else:
                                print("Invalid account number")
                        elif ch==4:                    
                            if ac in di.keys():
                                print("Which field you want to update ? \n1.Name\n2.phone ")
                                c=int(input("Enter your choice : "))
                                if c not in [1,2]:
                                    print("Enter the correct choice:")
                                else:
                                    if c==1:
                                        name=input("Enter the name :")
                                        di[ac]["name"]=name
                                        print(di)
                                        
                                    elif c==2:
                                        ph=int(input("Enter the phone number :"))
                                        di[ac]["ph"]=ph
                                        print(di)                            
                            else:
                                print("Invalid account number")
                






        



                

            



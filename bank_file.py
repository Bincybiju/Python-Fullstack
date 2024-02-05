d={"Bincy":"bincybiju","aby":"aby"}
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
                        ph=int(input("Enter phone number :"))
                        pin=int(input("Enter your pin :"))
                        bal=int(input("Enter the balance :"))
                        f=open(f"{ac}.txt","x")
                        f.close()
                        f=open(f"{ac}.txt","w")
                        f.write( f"{ac} \n{name} \n{ph}\n{pin}\n{bal}")
                        f.close()
                    elif c==2:
                        ac=int(input("Enter your account number :"))   
                        de=int(input("Enter the amount you want to deposit :"))
                        f=open(f"{ac}.txt","r")
                        l=f.readlines()
                        a=int(l[4])+de
                        f.close()
                        f=open(f"{ac}.txt","w")
                        l[4]=str(a)
                        f.writelines(l)
                        f.close()                         
                    elif c==3:
                        break
        elif num==2:
            ac=int(input("Enter your account number :"))           
            while True:
                print("1.Balance enquiry\n2.Deposit\n3.Withdrawal\n4.update details\n5.Exit")
                ch=int(input("Enter your choice :"))
                if ch not in [1,2,3,4]:
                    print("choose the correct option")
                elif ch==5:
                    break
                else:                                
                    if ch==1:
                        f=open(f"{ac}.txt","r")
                        l=f.readlines()
                        a=int(l[4])
                        print("Your current account balance :",a)
                        f.close()                      
                       
                    elif ch==2:
                            am=int(input("Amount that you want to deposit :"))
                            f=open(f"{ac}.txt","r")
                            l=f.readlines()
                            a=int(l[4])+am
                            f.close()
                            f=open(f"{ac}.txt","w")
                            l[4]=str(a)
                            f.writelines(l)
                            f.close()    
                            
                        
                    elif ch==3:
                            wi=int(input("Amount that you want to withdraw :"))
                            f=open(f"{ac}.txt","r")
                            l=f.readlines()
                            a=int(l[4])-wi
                            f.close()
                            f=open(f"{ac}.txt","w")
                            l[4]=str(a)
                            f.writelines(l)
                            f.close()
                            
                        
                    elif ch==4:                    
                            print("Which field you want to update ? \n1.Name\n2.phone ")
                            c=int(input("Enter your choice : "))     
                            if c==1:
                                name=input("Enter the name :")
                                f=open(f"{ac}.txt","r")
                                l=f.readlines()
                                # print(l)
                                a=l[1]
                                # print(a)
                                f.close()
                                f=open(f"{ac}.txt","w")
                                l[1]=name+"\n"
                                f.writelines(l)
                                # print(l)
                                f.close()  
                                
                                
                            elif c==2:
                                ph=int(input("Enter the phone number :"))
                                f=open(f"{ac}.txt","r")
                                l=f.readlines()
                                a=int(l[2])
                                f.close()
                                f=open(f"{ac}.txt","w")
                                l[2]=str(ph)+"\n"
                                f.writelines(l)
                                f.close() 
                                                     
                    
            






        



                

            



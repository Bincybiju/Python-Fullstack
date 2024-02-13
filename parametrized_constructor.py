# class A:
#     def __init__(self,fname):
#         self.name=fname
#     def display(self):
#         print(self.name)
# obj=A("Bincy")
# obj.display()
# obj2=A("Aby")
# obj2.display()

# class Car:
#     no=5
#     def __init__(self,eng_name):
#         print("The constructor is invoked")
#         self.color="white"
#         self.eng_name=eng_name
#     def start(self):
#         print(f"The car {self.rnum} has started")
#     def reg(self,rnum):
#         self.rnum=rnum
#         print(f"The car {self.rnum} is registered")      
#     def stop(self):
#         print(f"The car {self.rnum} is stopped")
#     def display(self):
#         print(f"The car {self.rnum} has {self.eng_name} engine and color is {self.color}")
# obj=Car("1.4 TDE")
# obj.reg("KL02AS2321")
# obj.start()
# obj.display()
# ob=Car("Fiat eng")
# obj.reg("KL02SW2321")
# obj.start()
# obj.display()

class Dogs:
    legs=4
    sound="Bark"
    def __init__(self,clr,brd):
        self.breed=brd
        self.color=clr
        print(f"It is a {clr} Dog")
    def naming(self,nm):
            self.dname=nm
    def sleep(self):
        print(f"{self.dname} is sleeping")
    def walk(self):
         print(f"Taking {self.dname} for a walk")
    def feed(self):
         print(f"Take the treat {self.dname}")
d1=Dogs("Black","Geerman shiphard")
d1.naming("Leo")
d2=Dogs("Black","Lab")
d2.naming("Rocky")
d1.walk()
d2.walk()
d1.feed()

    






# a=25
# b=35
# print(a+b)
# class A:
#     def __init__(self,a):
#         self.a=a 
#     def __add__(self,next):
#         print("sum is ")
#         print(self.a+next.a)
#     def __sub__(self,two):
#         print("Helo")
# ob1=A(5)
# ob2=A(4)
# ob1+ob2
# ob1-ob2



class A:
    def __init__(self,a):
        self.a=a 
    def __gt__(self,next):
        if self.a>next.a:
           print("greater")
        else:
            print("lesser")
    def __lt__(self,next):
        print("less than")
ob1=A(5)
ob2=A(4)
ob1<ob2
ob1>ob2

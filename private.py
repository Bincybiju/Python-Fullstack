class Base:
    def __init__(self):
        self._a=3
        print(self.__a)
        self.b=2
        print(self.b)
class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        # print("calling private member")#error
ob1=Base()
ob2=Derived()
print(ob1.b)
# print(ob1.__a)#error

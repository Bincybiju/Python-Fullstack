# class Car:
#     no=5
#     def start(self):
#         print("The car started")
#     def stop(self):
#         print("The car stopped")
# polo=Car()
# print(polo.no)
# polo.start()

# swift=Car()
# print(swift.no)
# swift.start()

# polo.stop()

class Car():
    no=5
    def start(self):
        print("The car is started")
    def reg(self,rnum):
        self.rnum=rnum
        print(f"The car {self.rnum} is registered")
    def stop(self):
        print("The car has stopped")
ob1=Car()
ob1.reg("KL02AG3241")
ob1.start()

ob2=Car()
ob2.reg("KL01AW2321")
ob2.start()
ob2.stop()

class Tvm:
    def knownfor(self):
        print("capital of kerala")
    def vehiclereg(self):
        print("KL01")
class Klm:
    def knownfor(self):
        print("It is known for cashew")
    def vehiclereg(self):
        print("KL02")
a=Tvm()
b=Klm()
for obj in a,b:
    obj.knownfor()
    obj.vehiclereg()
    
class Gfather:
    def __init__(self,gfathername):
        self.gfathername=gfathername
class Father(Gfather):
    def __init__(self,fathername,gfathername):
        self.fathername=fathername
        Gfather.__init__(self,gfathername)
class son(Father):
    def __init__(self,name,fathername,gfathername):
        self.name=name
        Father.__init__(self,fathername,gfathername)
    def print__out__(self):
        print("Grand Father :",self.gfathername)
        print("Father :",self.fathername)
        print("son :",self.name)
s=son("Antony","Mathew","Johnson")
print(s.gfathername)
print(s.fathername)
print(s.name)
s.print__out__()
f=Father("Mathew","Johnson")
# print(f.name) - Error
# print(f.print_out) - Error


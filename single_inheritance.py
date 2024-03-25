class Father:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(self.name)
class Child(Father):
    def __init__(self,name):
        self.name=name
f=Father("Arun")
c=Child("Anu")
f.show()
c.show()

class Father:
    fathername=""
    def father(self):
        print(self.fathername)
class Mother:
    mothername=""
    def mother(self):
        print(self.mothername)
class Child(Father,Mother):
    def parents(self):
        print("Father :",self.fathername)
        print("Mother :",self.mothername)
c=Child()
c.fathername="Arun"
c.mothername="Anu"
c.father()
c.mother()
c.parents()
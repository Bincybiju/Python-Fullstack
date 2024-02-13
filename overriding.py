class Bird:
    def intro(self):
        print("There are different varieties of birds")
    def flight(self):
        print("some can fly,some cannot")
class Sparrow(Bird):
    def flight(self):
        print("sparrow can fly")
class Ostrich(Bird):
    def flight(self):
        print("ostrich cannot fly")
b=Bird()
s=Sparrow()
o=Ostrich()
b.intro()
s.intro()
o.intro()
b.flight()
s.flight()
o.flight()
    
from abc import ABC,abstractmethod
class Animal(ABC):
    def living(self):
        print("Yes")
    @abstractmethod
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("can walk or run")
class Snake(Animal):
    def move(self):
        print("can scrawl")
s=Snake()
h=Human()
s.living()
s.move()
h.living()
h.move()

class Cats:
    leg=4
    sound="Meow"
    def __init__(self):
        print("It is a cat")
    def __del__(self):
        print("The destructor is called")
    def move(self):
        print("The cat can walk or run")
cc=Cats()
cc1=Cats()
cc.move()
del cc
cc1.move()

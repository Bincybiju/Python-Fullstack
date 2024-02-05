def display():
    '''This is to introduce how display works'''
    print("hello")
def show():
    print("Bye")
display()
show()
print(display.__doc__)

def sqr(x):
    print("square is :",x**2)
sqr(3)

# def add(a,b):
#     print("sum is :",a+b)
# x=int(input("Enter first number :"))
# y=int(input("Enter second number :"))
# add(x,y)

def add(a,b=0):
    print("sum is :",a+b)
add(2,5)
add(5)

def student(fn,ln,age=9):
    print(f"Hello {fn} {ln}")
    print(f"You are {age} years old")
student("Ammu","v",24)
student(fn="Anu",ln="L",age=23)
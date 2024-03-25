x=10 #global
def change():
    x=30 #local
    print(x)
print(x)
change()
print(x)

x=10
def func():
    y=20
    print(y)
print(x)
func()
# print(y) #not defined

x=20
def f1():
    y=10
    print("inside function",x,y)
def f2():
    print("inside function",x)
    # print("inside function",y) #nameerror
f1()
f2()
print("outside fn",x)

x=10
def change():
    global x
    x=20
    print(x)
print(x)
change()
print(x)

def func1():
    global x
    x=10
    print("inside function",x)
def func2():
    y=15
    print("outside function1 and inside function2",x)
    print("sum",x+y)
func1()
print("outside function",x)
func2()

#pass by value

a=10
def sum(a):
    a=a+20
    print(a)
sum(a)
print(a)

#pass by reference

l=[2,4,6,8]
def inserting(l):
    l.append(10)
inserting(l)
print(l)
    
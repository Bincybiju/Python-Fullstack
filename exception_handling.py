a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
try:
    print(a/b)
except:
    print("There is zero division error")
print("Helo")

def func(num):
    if num<4:
        b=num/(num-3)
    print("output",b)
try:
    func(5)
except ZeroDivisionError:
    print("Division by zero is not possible")
except NameError:
    print("output cannot be displayed")
except:
    print("error occured")
else:
    print("else is working")
finally:
    print("finally printed")
print("After exception handling")
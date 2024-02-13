class A:
    def ___init__(self):
        self._a=2
        print(self._a)
class B(A):
    def __init__(self):
        A.___init__(self)
        print("Accessing protected member")
        self._a=5
        print(self._a)
ob=A()
ob1=B()
print(ob._a)
print(ob1._a)


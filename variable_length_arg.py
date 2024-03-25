#Non keyword argument

# def details(*args):
#     for i in args:
#         print(i)
# details("achu",23,"dev")

# def detail(name,*args):
#     print(type(args))
#     print("hello",name)
#     for i in args:
#         print(i)
# detail("Anu",23,"kannur")
# detail("Achu","kollam")

# def add(*num):
#     s=0
#     for i in num:
#         s=s+i
#     print(s)
# add(2,3,4)
# add(5)
# add(3,4,5,6,7)


#keyword argument

# def employee(**kwargs):
#     for i,j in kwargs.items():
#         print(i,j,sep="-")
# employee(name="Ammu",age=23,salary=23000)

# def employee(**kwargs):
#     for i in kwargs.values():
#         print(i)
# employee(name="Ammu",age=23,salary=23000)

# def employee(name,**kwargs):
#     print("Hello",name)
#     for i in kwargs.values():
#         print(i)
# employee(name="Ammu",age=23,salary=23000)

#Return

# def add(x,y):
#     print(f"The sum of {x} and {y} is :")
#     return x+y
# s=add(5,6)
# print(s)

 
import time
def sqr(a):
    for i in a :
        time.sleep(1)
        print(i**2)
def cube(a):
    for i in a:
        time.sleep(1)
        print(i**3)
t1=time.time()
l=[2,3,4,5]
sqr(l)
cube(l)

print(time.time()-t1)

    
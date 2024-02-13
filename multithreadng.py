import time
import threading
def sqr(a):
    for i in a :
        time.sleep(1)
        print("sqr",i**2)
def cube(a):
    for i in a:
        time.sleep(1)
        print("cube",i**3)
t1=time.time()
l=[2,3,4,5]
th1=threading.Thread(target=sqr,args=(l,))
th2=threading.Thread(target=cube,args=(l,))
th1.start()
th2.start()
th1.join()
th2.join()
print(time.time()-t1)

    
s=lambda x:x**2
print(s(5))

p=lambda a,b:a*b
print(p(3,4))

# filter()

l=[1,2,3,4,5,6]
nl=list(filter(lambda x:x%2==0,l))
print(nl)

#map()

l=[1,2,3,4,5,6]
ml=list(map(lambda x:x*2,l))
print(ml)

# reduce()

from functools import reduce
l=[1,2,3,4,5,6]
m=reduce(lambda x,y:x+y,l)
print(m)

p=lambda x,y:x*y
print(p(3,4))


m=lambda x:x+15
print(m(3))






#type

a=()
c=tuple()
print(a,type(a),sep="\n")
print(type(c))

t=1,2,3 #without paranthesis
print(type(t))

#index

t=(1,2,3)
print(t[0])

#immutable

# t[0]=10
# print(t)
# del(t[1])
# print(t)

#Tuple unpacking 

t=("hi","good","morning")
x,y,z=t
print(x)
print(y)
print(z)

a,b=10,20
print(a)
print(b)

#swapping

a,b=1,2
a,b=b,a
print(a)
print(b)

#asthetic *

t=("hi","how","old","are","you")
i,*j=t
print(i)
print(j)#store as list

i,*j,k=t
print(i)
print(j)
print(k)

*i,j,k=t
print(i)
print(j)
print(k)

#convert list to tuple

l=[1,2,3]
t=tuple(l)
print(l)
print(t)

#iterating through loop

for i in t:
    print(i)

for i in range(len(t)):
    print(t[i])

#Add two tuple

l=(1,2,3)
li=("hi","hai")
print(l+li)

print(l*3)

#tuple methods

#count
t=(1,2,3,3,2,4,5)
print(t.count(2))


#index
print(t.index(2))

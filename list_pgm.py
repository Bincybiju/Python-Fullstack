# l=[]
# print(type(l))

#Indexing
l=[1,2,3.5,"hi"]
print(l[1])
print(l[3])
print(l[3][1])

#slicing
print(l[1:4])

#update
l[1]=0
print(l)

#insertion

#append
l.append("hello")
print(l)
l.append(10)
print(l)
l.append([1,2])
print(l)

#extend
l.extend("helo")
print(l)
l.extend([4,9])
print(l)

#insert
l.insert(1,30)
print(l)

#deletion

#pop()
l=[1,2,3,4,5]
c=l.pop()
#retrieve pop element
print(c)
l.pop(2)
print(l)#index

#remove()
l.remove(1)
print(l)

#clear
l.clear()
print(l)

# del keyword
l=[1,2,3,4,5]
del(l[2])
print(l)
# del l
# print (l)
#l is not defined

l=list(range(1,11))
print(l)

#itrating list
l=[1,2,3,4,5]
for i in l:
    print(i)
print()
for i in range(len(l)):
    print(l[i])


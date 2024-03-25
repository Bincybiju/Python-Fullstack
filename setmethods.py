# add()

c=set()
c.add(15)
print(c)
c.add((16,17))
print(c)

#update()

d={1,2,3,4}
e={2,3,5,6}
e.update(d)
print(e)

s1=set(["python","for","all"])
print(s1)

print("python" in s1)

# remove()

a={1,2,3,4}
a.remove(1)
print(a)
# a.remove(5)
# print(a) error bcoz 5 is not an element in a

#discard

a.discard(2)
print(a)
a.discard(5) #5 not in a ,but output willshown
print(a) #this code will execute

# frozenset()

s1=frozenset(a)
print(s1)

# s1.discard(3) # discard not possible in frozenset 
# print(s1)

# union()

a={1,2,3,4,5}
b={4,5,6,7,8}
print(a.union(b))

#difference()

print(a.difference(b))
print(b.difference(a))

#difference_update()

b.difference_update(a)
print(b)

#intersection()

a={1,2,3,4,5}
b={4,5,6,7,8}
c=a.intersection(b)
print(c)

#intersection_update()

a.intersection_update(b)
print(a)

# disjoint()

a={1,2}
b={3,4}
print(a.isdisjoint(b))

a={1,2,3}
b={3,4}
print(a.isdisjoint(b))







l=[2,3,4,1]

#sum
print("sum is " ,sum(l))

#sort ascending
l.sort()
print("Ascending order :", l)

#sort descending
l.sort(reverse=True)
print("Descending order :",l)

l=["A","B","Zoo","zip","and","ammu"]
l.sort()
print("Ascending order :", l)

#index
print("index is",l.index("B"))

#reverse
l.reverse()
print("reverse",l)#count
# l.count()

#copy
l=[1,2,3,4,2]
li=l.copy()
li.append(5)
print(li)
print(l)

#count
l.count(2)
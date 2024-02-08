l=[2,0,3,0,5,0,0,1,0,8]
# c=l.count(0)
# print(c)
# l.sort()
# print(l)
# for i in range(c):
#     l.remove(0)
#     l.append(0)
# print(l) 


l.sort()
for i in l:
    if i==0:
        c=l.pop(l.index(i))
        l.append(c) 
        print(l)

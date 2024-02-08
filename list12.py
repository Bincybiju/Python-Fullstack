l1=[[1,2],[2,3]]
l2=[[2,3],[4,5]]
l=[[0,0],[0,0]]
for i in range(len(l1)):
    for j in range(len(l1[0])):
        if len(l1)==len(l2) and len(l1[0])==len(l2[0]):
            l[i][j]=l1[i][j]+l2[i][j]
            print(l[i][j],end=" ")
    print() 
l1=[[1,2],[2,3]]
l2=[[2,3],[4,5]]
f=0
if len(l1)==len(l2) and len(l1[0])==len(l2[0]):
    for i in range(len(l1)):
        for j in range(len(l1[0])):
            if l1[i][j]!=l2[i][j]:
                f=1               
if f==0:
    print("Matrix are same")
else:
    print("Matrix are not same")


   
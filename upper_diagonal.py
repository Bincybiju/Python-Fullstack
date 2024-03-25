l=[[1,25,3],[4,5,6],[7,8,9]]
n=len(l)
for i in range(n):
    for j in range(n):
        if(i>j):
            l[i][j]=1
        elif i<j:
            l[i][j]=0
for i in l:
    print(i)  
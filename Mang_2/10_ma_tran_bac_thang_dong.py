r,c=map(int,input().split())
mat=[list(map(int,input().split())) for _ in range(r)]
for i in range(r):
    for j in range(c):
        if j<i:
            print(0,end=" ")
        else:
            print(mat[i][j],end=" ")
    print()
r,c=map(int,input().split())
mat=[list(map(int,input().split())) for _ in range(r)]
for i in range(r):
    print("Max hang",i+1,"=",max(mat[i]))
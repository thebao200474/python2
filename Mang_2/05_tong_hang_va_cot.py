r,c=map(int,input().split())
mat=[list(map(int,input().split())) for _ in range(r)]
for i in range(r):
    print("Tong hang",i+1,"=",sum(mat[i]))
for j in range(c):
    print("Tong cot",j+1,"=",sum(mat[i][j] for i in range(r)))
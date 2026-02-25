n=int(input())
mat=[list(map(int,input().split())) for _ in range(n)]
tong=sum(mat[i][i] for i in range(n))
print(tong)
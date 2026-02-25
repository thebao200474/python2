n=int(input())
A=[list(map(int,input().split())) for _ in range(n)]
B=[list(map(int,input().split())) for _ in range(n)]
C=[[A[i][j]+B[i][j] for j in range(n)] for i in range(n)]
for row in C:
    print(row)
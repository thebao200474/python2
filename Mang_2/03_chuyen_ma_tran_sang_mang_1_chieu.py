n=int(input())
mat=[list(map(int,input().split())) for _ in range(n)]
arr=[]
for row in mat:
    arr.extend(row)
print(arr)
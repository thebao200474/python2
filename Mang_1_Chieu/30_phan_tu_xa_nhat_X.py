arr=list(map(int,input().split()))
X=int(input())
print(max(arr,key=lambda x:abs(x-X)))
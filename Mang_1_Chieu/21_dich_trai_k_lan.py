arr=list(map(int,input().split()))
k=int(input())
k%=len(arr)
print(arr[k:]+arr[:k])
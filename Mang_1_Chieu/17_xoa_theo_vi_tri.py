arr=list(map(int,input().split()))
pos=int(input())
if 1<=pos<=len(arr):
    arr.pop(pos-1)
print(arr)
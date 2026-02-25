n=int(input())
arr=[]
while len(arr)<n:
    x=int(input())
    if x not in arr:
        arr.append(x)
print(arr)
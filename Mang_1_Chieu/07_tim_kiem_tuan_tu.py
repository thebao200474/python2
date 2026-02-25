arr=list(map(int,input().split()))
x=int(input())
print(arr.index(x)+1 if x in arr else "Khong tim thay")
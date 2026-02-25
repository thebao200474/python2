arr=list(map(int,input().split()))
le=[x for x in arr if x%2!=0]
print(max(le) if le else "Khong co")
arr=list(map(int,input().split()))
chan=[x for x in arr if x%2==0]
le=[x for x in arr if x%2!=0]
print("Chan:",chan)
print("Le:",le)
def prime(x):
    if x<2:return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:return False
    return True

arr=list(map(int,input().split()))
snt=[x for x in arr if prime(x)]
print(max(snt) if snt else "Khong co")
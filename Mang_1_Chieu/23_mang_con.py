A=list(map(int,input().split()))
B=list(map(int,input().split()))
for i in range(len(A)-len(B)+1):
    if A[i:i+len(B)]==B:
        print("La mang con")
        break
else:
    print("Khong phai")
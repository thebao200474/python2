arr=list(map(int,input().split()))
if arr==sorted(arr):
    print("Tang")
elif arr==sorted(arr,reverse=True):
    print("Giam")
else:
    print("Ngau nhien")
import math
a,b=map(int,input().split())
if b==0:
    print("Khong hop le")
else:
    g=math.gcd(a,b)
    a//=g; b//=g
    if b<0:
        a=-a; b=-b
    print(a if b==1 else f"{a}/{b}")
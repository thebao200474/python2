import math
a,b,c = map(float,input("Nhap a b c: ").split())
if a==0:
    print("PT bac 1, x =", -c/b)
else:
    d=b*b-4*a*c
    if d<0:
        print("Vo nghiem")
    elif d==0:
        print("Nghiem kep =", -b/(2*a))
    else:
        print("x1 =", (-b+math.sqrt(d))/(2*a))
        print("x2 =", (-b-math.sqrt(d))/(2*a))
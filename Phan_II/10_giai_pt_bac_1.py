a,b = map(float,input("Nhap a b: ").split())
if a==0:
    print("Vo so nghiem" if b==0 else "Vo nghiem")
else:
    print("x =", -b/a)
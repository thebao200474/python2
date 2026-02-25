import math
a,b,c = map(float,input("Nhap 3 canh: ").split())
if a+b>c and a+c>b and b+c>a:
    p=(a+b+c)/2
    s=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("Dien tich =", s)
else:
    print("Khong phai tam giac")
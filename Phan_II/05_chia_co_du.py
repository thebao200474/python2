a,b = map(int,input("Nhap a b: ").split())
if b==0:
    print("Khong hop le")
elif a%b==0:
    print(f"{a} / {b} = {a//b}")
else:
    print(f"{a} / {b} = {a//b}, du {a%b}")
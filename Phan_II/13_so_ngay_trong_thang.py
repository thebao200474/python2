m = int(input("Nhap thang: "))
if m in [1,3,5,7,8,10,12]:
    print("31 ngay")
elif m in [4,6,9,11]:
    print("30 ngay")
elif m==2:
    print("28 hoac 29 ngay")
else:
    print("Khong hop le")
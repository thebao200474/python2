y = int(input("Nhap nam: "))
if (y%4==0 and y%100!=0) or y%400==0:
    print("Nam nhuan")
else:
    print("Khong phai nam nhuan")
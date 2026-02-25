sp = int(input("Nhap so san pham: "))
luong = 300
gia = 450
if 1<=sp<=3: hh=0.02
elif 4<=sp<=6: hh=0.03
elif 7<=sp<=9: hh=0.04
else: hh=0.05
print("Tong luong =", luong + sp*gia*hh)
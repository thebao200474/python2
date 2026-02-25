h,m,s = map(int,input("Nhap gio phut giay: ").split())
n = int(input("Nhap N giay: "))
tong = h*3600 + m*60 + s + n
h = (tong//3600)%24
m = (tong%3600)//60
s = tong%60
print(f"{h}:{m}:{s}")
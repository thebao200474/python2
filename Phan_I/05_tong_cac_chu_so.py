n = abs(int(input("Nhap so <1000: ")))
tong = 0
while n > 0:
    tong += n % 10
    n //= 10
print("Tong =", tong)
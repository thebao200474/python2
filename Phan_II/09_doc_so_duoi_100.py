so = ["khong","mot","hai","ba","bon","nam","sau","bay","tam","chin"]
n = int(input("Nhap so <100: "))
if n<10:
    print(so[n])
else:
    print(so[n//10], "muoi", so[n%10])
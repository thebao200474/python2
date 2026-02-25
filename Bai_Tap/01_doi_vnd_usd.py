choice = input("Nhap VND hoac USD: ")
amount = float(input("Nhap so tien: "))
if choice.upper() == "USD":
    print("VND =", amount * 22700)
else:
    print("USD =", amount / 22700)
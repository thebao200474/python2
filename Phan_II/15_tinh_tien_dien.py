cu,moi = map(int,input("Nhap chi so cu moi: ").split())
kwh = moi - cu
tien = 0
if kwh<=50:
    tien = kwh*1400
elif kwh<=100:
    tien = 50*1400 + (kwh-50)*1500
elif kwh<=200:
    tien = 50*1400 + 50*1500 + (kwh-100)*1800
elif kwh<=300:
    tien = 50*1400 + 50*1500 + 100*1800 + (kwh-200)*2200
else:
    tien = 50*1400 + 50*1500 + 100*1800 + 100*2200 + (kwh-300)*2500
print("Tien phai tra =", tien*1.1)
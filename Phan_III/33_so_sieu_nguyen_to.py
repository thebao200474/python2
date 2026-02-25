def prime(x):
    if x<2:return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:return False
    return True

n=int(input())
temp=n
while temp>0:
    if not prime(temp):
        print("Khong phai")
        break
    temp//=10
else:
    print("Sieu nguyen to")
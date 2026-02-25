n=int(input())
tong=sum(i for i in range(1,n) if n%i==0)
print("Hoan hao" if tong==n else "Khong")
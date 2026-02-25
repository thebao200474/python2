n=int(input())
if n<2:
    print("Khong phai SNT")
else:
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            print("Khong phai SNT")
            break
    else:
        print("La SNT")
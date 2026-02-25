def prime(x):
    if x<2:return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:return False
    return True

n=int(input())
if prime(n):
    print("La SNT")
else:
    for i in range(n-1,1,-1):
        if prime(i):
            print(i)
            break
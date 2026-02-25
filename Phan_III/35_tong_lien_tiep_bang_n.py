n=int(input())
found=False
for i in range(1,n):
    s=0
    j=i
    while s<n:
        s+=j
        j+=1
        if s==n:
            print(" + ".join(map(str,range(i,j))))
            found=True
            break
if not found:
    print("Khong ton tai")
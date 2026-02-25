import math
a,b=map(int,input().split())
print("UCLN =",math.gcd(a,b))
print("BCNN =",abs(a*b)//math.gcd(a,b))
x=float(input())
y=1
while abs(y - x/y) > 1e-6:
    y=(y + x/y)/2
print(y)
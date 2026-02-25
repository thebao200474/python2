arr=list(map(int,input().split()))
lst=[x for x in arr if x%3==0]
print("Tong =",sum(lst))
print("TB =",sum(lst)/len(lst) if lst else 0)
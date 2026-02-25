arr=list(map(int,input().split()))
B,C=map(int,input().split())
lst=[x for x in arr if x<C and x%2==0]
print(sum(lst[:B]))
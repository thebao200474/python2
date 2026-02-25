n = int(input("Nhap N: "))
matrix = [list(map(int,input().split())) for _ in range(n)]
print("Tong duong cheo chinh =", sum(matrix[i][i] for i in range(n)))
n = int(input())
matrix = [[int("0") for _ in range(n)] for _ in range(n)]

for i in range(n):
	for j in range(n):
		if i + j + 1 == n:
			matrix[i][j] = int("1")
		if ((i > j and i > n - 1 - j) or (i < j and i > n - 1 - j)) or i + j + 1 > n:
			matrix[i][j] = int("2")

for k in range(n):
	print(*matrix[k])
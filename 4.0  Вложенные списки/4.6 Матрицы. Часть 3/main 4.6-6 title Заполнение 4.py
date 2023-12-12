n = int(input())

matrix = [[str(0) for _ in range(n)] for _ in range(n)]

for i in range(n):
	for j in range(n):
		if (i == j) or (i + j + 1 == n) or (i < j and i < n - 1 - j) or (i > j and i > n - 1 - j):
			matrix[i][j] = "1"
	print(*matrix[i])
n = int(input())

matrix = [[str("0").ljust(3) for _ in range(n)] for _ in range(n)]

for i in range(n):
	for j in range(n):
		if i == j or i + j + 1 == n:
			matrix[i][j] = "1".ljust(3)

for k in range(n):
	print(*matrix[k])
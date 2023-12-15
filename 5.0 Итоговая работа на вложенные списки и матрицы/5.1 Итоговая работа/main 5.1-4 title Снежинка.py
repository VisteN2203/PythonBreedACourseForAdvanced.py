n = int(input())

matrix = [[str(".") for _ in range(n)] for _ in range(n)]


for i in range(n):
	for j in range(n):
		if i == j or i + j + 1 == n:
			matrix[i][j] = "*"
		if n // 2 == j or n // 2 == i:
			matrix[i][j] = "*"



for k in range(n):
	print(*matrix[k])
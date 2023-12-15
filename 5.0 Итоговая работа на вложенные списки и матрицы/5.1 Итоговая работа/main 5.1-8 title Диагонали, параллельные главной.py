n = int(input())

matrix = [[int(0) for _ in range(n)] for _ in range(n)]

for q in range(n):
	for i in range(n):
		for j in range(n):
			if q == i - j or q == j - i:
				matrix[i][j] = q

for k in range(n):
	print(*matrix[k])
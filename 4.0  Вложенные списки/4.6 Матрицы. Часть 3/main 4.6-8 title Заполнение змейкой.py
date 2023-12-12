text = list(input().split())
n,m = int(text[0]),int(text[1])

matrix = [[str("").ljust(3) for _ in range(m)] for _ in range(n)]

for i in range(n):
	for j in range(m):
		if i % 2 == 0:
			matrix[i][j] = str(i * m + j + 1)
		else:
			matrix[i][-j - 1] = str(i * m + j + 1)

for k in range(n):
	print(*matrix[k])
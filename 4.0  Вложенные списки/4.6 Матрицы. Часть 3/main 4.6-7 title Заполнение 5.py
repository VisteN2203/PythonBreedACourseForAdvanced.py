text = list(input().split())
n,m = int(text[0]),int(text[1])

matrix = [[str("") for _ in range(m)] for _ in range(n)]

for i in range(n):
	for j in range(m):
		matrix[i][j] = (i + j) % m + 1

for k in range(n):
	print(*matrix[k])



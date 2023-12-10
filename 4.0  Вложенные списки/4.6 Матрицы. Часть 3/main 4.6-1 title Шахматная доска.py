x = list(input().split())
n,m = int(x[0]),int(x[1])

matrix = [[str(".") for q in range(m)] for _ in range(n)]

for i in range(n):
	for j in range(m):
		if j % 2 != 0 and i % 2 == 0:
			matrix[i][j] = "*"
		elif j % 2 == 0 and i % 2 != 0:
			matrix[i][j] = "*"

for k in range(n):
	print(*matrix[k])
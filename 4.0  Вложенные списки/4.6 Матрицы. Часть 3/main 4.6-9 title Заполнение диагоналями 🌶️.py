text = list(input().split())
n,m = int(text[0]),int(text[1])

matrix = [[str("").ljust(3) for _ in range(m)] for _ in range(n)]

nm = 0
for q in range(n * m):
	for i in range(n):
		for j in range(m):
			if i + j == q:
				nm += 1
				matrix[i][j]= nm

for k in range(n):
	print(*matrix[k])
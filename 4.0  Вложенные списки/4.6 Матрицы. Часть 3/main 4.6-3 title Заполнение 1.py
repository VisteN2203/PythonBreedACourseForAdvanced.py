text = list(input().split())
n,m = int(text[0]),int(text[1])


matrix = [[int(0) for _ in range(m)] for _ in range(n)]

total = 0
for i in range(n):
	for j in range(m):
		total += 1
		matrix[i][j] = int(str(total).ljust(3))

for k in range(n):
	print(*matrix[k])

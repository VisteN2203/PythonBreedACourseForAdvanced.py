n = int(input())

matrix = [[int(q) for q in input().split()] for _ in range(n)]

for i in range(n):
	matrix[i][i],matrix[n-1-i][i] = matrix[n-1-i][i],matrix[i][i]

for j in range(n):
	print(*matrix[j])

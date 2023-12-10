n = int(input())

matrix = [[int(q) for q in input().split()] for _ in range(n)]

# matrix.reverse()
# for i in range(n):
# 	print(*matrix[i])

for i in range(n):
	for j in range(n):
		matrix[i][i] = matrix[i][n-i-1]

print(matrix)

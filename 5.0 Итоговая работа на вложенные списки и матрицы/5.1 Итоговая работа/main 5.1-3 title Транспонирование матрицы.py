n = int(input())

matrix_original = [input().split() for _ in range(n)]

matrix_modification = [[str("0") for _ in range(n)] for _ in range(n)]

for i in range(n):
	for j in range(n):
		matrix_modification[j][i] = matrix_original[i][j]


for k in range(n):
	print(*matrix_modification[k])


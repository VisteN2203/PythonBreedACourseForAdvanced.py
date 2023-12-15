n_m = int(input())

matrix_one = [[int(p) for p in input().split()] for _ in range(n_m)]
matrix_two = matrix_one

matrix_final = [[int(0) for _ in range(n_m)] for _ in range(n_m)]


degree = int(input())
for k in range(1,degree):
	matrix_final = [[int(0) for _ in range(n_m)] for _ in range(n_m)]
	for q in range(n_m):
		for i in range(n_m):
			for j in range(n_m):
				matrix_final[q][i] += matrix_one[q][j] * matrix_two[j][i]
	matrix_one = matrix_final


for k in range(n_m):
	print(*matrix_final[k])
data_matrix_one = list(input().split())
n_one,m_one = int(data_matrix_one[0]),int(data_matrix_one[1])

matrix_one = [[int(p) for p in input().split()] for _ in range(n_one)]

space = input()

data_matrix_two = list(input().split())
n_two,m_two = int(data_matrix_two[0]),int(data_matrix_two[1])

matrix_two = [[int(p) for p in input().split()] for _ in range(n_two)]

matrix_three = [[int(0) for _ in range(m_two)] for _ in range(n_one)]

for q in range(n_one):
	for i in range(n_one):
		for j in range(m_one):
			matrix_three[q][i] += matrix_one[q][j] * matrix_two[j][i]

for k in range(n_one):
	print(*matrix_three[k])
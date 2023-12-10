n,m = int(input()),int(input())
list = []
[list.append(str(input()).split()) for _ in range(n)]

maximum_number = - 99999
matrix_number = 0
number_of_the_number = 0
for i in range(len(list)):
	for j in range(m):
		if int(list[i][j]) > maximum_number:
			maximum_number = int(list[i][j])
			matrix_number = i
			number_of_the_number = j

print(matrix_number, number_of_the_number)


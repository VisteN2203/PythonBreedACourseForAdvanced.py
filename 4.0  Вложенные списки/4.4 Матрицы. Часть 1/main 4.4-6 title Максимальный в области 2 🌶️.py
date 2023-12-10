n = int(input())
matrix = []
list = []

[matrix.append(str(input()).split()) for k in range(n)]

for i in range(n):
	for j in range(n):
		if (i >= j and i <= n - 1 - j) or (i <= j and i >= n - 1 - j):
			list.append(int(matrix[i][j]))
print(max(list))
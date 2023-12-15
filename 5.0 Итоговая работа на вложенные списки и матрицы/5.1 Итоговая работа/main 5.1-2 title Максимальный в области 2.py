n = int(input())
matrix = [input().split() for _ in range(n)]
list_max = []
for i in range(n):
	for j in range(n):
		if (i <= j and i >= n - 1 - j) or (i >= j and i >= n - 1 - j):
			list_max.append(matrix[i][j])

print(max(list_max))
n = int(input())

matrix = [[int(q) for q in input().split()] for _ in range(n)]

for i in range(n):
	for j in range(n):
		print(matrix[n-j-1][i],end=" ")
	print()
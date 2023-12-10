n = int(input())

matrix = [[int(q) for q in input().split()] for _ in range(n)]

for i in range(n - 1, -1 , -1):
		print(*matrix[i])


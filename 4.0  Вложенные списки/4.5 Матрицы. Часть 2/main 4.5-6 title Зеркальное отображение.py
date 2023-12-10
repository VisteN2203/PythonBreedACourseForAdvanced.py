n = int(input())

matrix = [[int(q) for q in input().split()] for _ in range(n)]

# matrix.reverse()
# for i in range(n):
# 	print(*matrix[i])

for i in range(n - 1, -1 , -1):
		print(*matrix[i])

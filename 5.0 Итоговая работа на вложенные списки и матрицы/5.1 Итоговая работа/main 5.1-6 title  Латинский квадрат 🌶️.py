n = int(input())

matrix = [[int(q) for q in input().split() ]for _ in range(n)]

summa = sum([k for k in range(1,n + 1)])

flag = True
for i in range(n):
	for j in range(n):
		summa_y = 0
		for l in range(n):
			summa_y += matrix[l][j]
		if sum(matrix[i]) != summa or summa_y != summa:
			flag = False
			break


if flag == True:
	print("YES")
elif flag == False:
	print("NO")

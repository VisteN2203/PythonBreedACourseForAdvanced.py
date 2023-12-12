text = list(input().split())
n,m = int(text[0]),int(text[1])

matrix_one,matrix_two,matrix_three = [],[],[[str("0") for _ in range(m)] for _ in range(n)]
[matrix_one.append(str(input()).split()) for _ in range(n)]
space = input()
[matrix_two.append(str(input()).split()) for _ in range(n)]



for i in range(n):
	for j in range(m):
		matrix_three[i][j] = int(matrix_one[i][j],) + int(matrix_two[i][j])

for k in range(n):
	print(*matrix_three[k])
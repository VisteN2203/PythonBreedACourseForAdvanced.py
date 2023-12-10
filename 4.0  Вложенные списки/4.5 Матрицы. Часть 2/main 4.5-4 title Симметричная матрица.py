n = int(input())

list = [[int(i) for i in input().split()] for _ in range(n)]

flag=True
for i in range(n):
	for j in range(n):
		if list[i][j] != list[j][i]:
			flag=False

if flag == True:
	print("YES")
elif flag == False:
	print("NO")
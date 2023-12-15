n = int(input())

list = [[int(i) for i in input().split()] for _ in range(n)]

flag=True
for i in range(n):
	for j in range(n):
		if list[i][j] != list[n-j-1][n-i-1]:
			flag=False

if flag == True:
	print("YES")
elif flag == False:
	print("NO")